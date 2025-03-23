from pyautogui import typewrite
from time import sleep

def type (text : str) :

    sleep(3)
    typewrite(text, interval=0.05)

