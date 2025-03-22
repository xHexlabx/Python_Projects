import keyboard
import time
import pyautogui
from ElswordBot.modules import get_object_position, follow

def track_character(image_path , screen_center , delay):
    """Track and follow the main character in Elsword."""
    print("Elsword Bot Activated! Press 'q' to stop.")

    while not keyboard.is_pressed("q"):  # Press 'q' to stop
        position = get_object_position(image_path)
        if position:
            print(f"🎯 Found {image_path} at {position}")
            follow(position, screen_center)
        time.sleep(delay)  # Prevent excessive CPU usage

    print("Elsword Bot Stopped!")