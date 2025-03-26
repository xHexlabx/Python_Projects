import pyautogui

def screen_capture (x1: int, y1: int, x2: int, y2: int) :
    width = x2 - x1
    height = y2 - y1
    screenshot = pyautogui.screenshot(region=(x1, y1, width, height))

    return screenshot