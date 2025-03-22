import keyboard
import time
import pyautogui
from ElswordBot.modules import get_object_position, follow , track_character

# Configuration
IMAGE_PATH = './images/main_character.png'
SCREEN_CENTER = (1440, 900)  # Screen resolution: 2880x1800
DELAY = 1  # Time interval between scans

def main():

    print("Elsword Bot is running...🤖\nPress '1' to start tracking...")
    keyboard.wait("1")
    track_character(image_path = IMAGE_PATH , screen_center = SCREEN_CENTER , delay = DELAY)

if __name__ == "__main__":
    main()
