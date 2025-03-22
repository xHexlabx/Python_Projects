import pyautogui
import time

def VS_Seekers():

    for i in range(15) :

        pyautogui.keyDown("a")  # Press and hold "A"
        pyautogui.keyDown("k")  # Press and hold "A"
        time.sleep(0.05)  # Hold for 5 seconds
        pyautogui.keyUp("a")  # Release "A"
        pyautogui.keyUp("k")  # Release "A"

        time.sleep(0.1)

        pyautogui.keyDown("d")  # Press and hold "A"
        pyautogui.keyDown("k")  # Press and hold "A"
        time.sleep(0.1)  # Hold for 5 seconds
        pyautogui.keyUp("d")  # Release "A"
        pyautogui.keyUp("k")  # Release "A"

    pyautogui.keyDown("u")  # Press and hold "A"
    time.sleep(0.1)  # Hold for 5 seconds
    pyautogui.keyUp("u")  # Press and hold "A"

    pyautogui.keyDown("d")  # Press and hold "A"
    time.sleep(0.3)  # Hold for 5 seconds
    pyautogui.keyUp("d")  # Press and hold "A"

    pyautogui.keyDown("j")  # Press and hold "A"
    time.sleep(0.1)  # Hold for 5 seconds
    pyautogui.keyUp("j")  # Press and hold "A"