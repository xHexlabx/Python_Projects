import pyautogui
import time

def Battle ():

    for i in range(15) :

        pyautogui.keyDown("j")  # Press and hold "A"
        time.sleep(0.5)  # Hold for 5 seconds
        pyautogui.keyUp("j")  # Release "A"

    for i in range(10) :

        pyautogui.keyDown("k")  # Press and hold "A"
        time.sleep(0.5)  # Hold for 5 seconds
        pyautogui.keyUp("k")  # Release "A"

    for i in range(15) :

        pyautogui.keyDown("j")  # Press and hold "A"
        time.sleep(0.5)  # Hold for 5 seconds
        pyautogui.keyUp("j")  # Release "A"

