import pynput


def process_key_press(key):
    print(key)
keyboard_Listener = pynput.keyboard.Listener(on_press = process_key_press)