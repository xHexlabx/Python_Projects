from . import get_object_position
import time
import pyautogui

def follow (position , center_point) :
    x , y = position
    if x < center_point[0] and abs(x - center_point[0]) > 100:
        print('a')
        pyautogui.keyDown('a')
        time.sleep(0.5)
        pyautogui.keyUp('a')
    elif x > center_point[0] and abs(x - center_point[0]) > 100:
        print('d')
        pyautogui.keyDown('d')
        time.sleep(0.5)
        pyautogui.keyUp('d')

    return