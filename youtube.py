from pynput.keyboard import Key, Controller

keyboard = Controller()

def playPause():
    keyboard.press(Key.space)
    keyboard.release(Key.space)
