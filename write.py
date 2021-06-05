import keyboard
from pynput.keyboard import Key, Controller

keyboard2 = Controller()

def escrever(text):
    resultado = ""
    resultado = text.replace('inteligência escreva ', "")
    if "inter" in text or "enter" in text :
        resultado = resultado.replace("inter", "")
        resultado = resultado.replace("enter", "")
        keyboard2.press(Key.enter)
        keyboard2.release(Key.enter)
    keyboard.write(resultado)
