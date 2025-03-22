import keyboard
import time
import pyautogui
from ElswordBot.modules import get_character_position

def track_character(model, delay: float):
    """Track and follow the main character in Elsword."""
    print("Elsword Bot Activated! Press 'q' to stop.")

    while not keyboard.is_pressed("q"):  # Press 'q' to stop
        screenshot = pyautogui.screenshot()
        position = get_character_position(model, screenshot)

        if position != None:
            x,y,w,h = position[0]
            print(f"🎯 Found character at {x} {y}")
            # follow(position, screen_center)
        else:
            print("⚠️ Character not found!")

        time.sleep(delay)  # Prevent excessive CPU usage

    print("Elsword Bot Stopped!")
