import time

from modules import ocr, type, data_screen_capture, screen_capture
import keyboard

SCREEN_POSITION = {
    "x1": 432,
    "y1": 800,
    "x2": 2600,
    "y2": 900,
    "interval_seconds": 0.5,
    "output_folder": "./images"
}

SCREEN_POSITION_2 = {
    "x1": 432,
    "y1": 800,
    "x2": 2600,
    "y2": 900,
}

def main():
    print("TypeBreaker is ready. Press Enter to start, and press Enter again to stop.")
    keyboard.wait("enter")  # Wait for first Enter press to start
    print("TypeBreaker is running 🤖")

    time.sleep(2)

    while True:
        if keyboard.is_pressed("enter"):  # Stop if Enter is pressed again
            print("TypeBreaker is stopping...")
            break

        screenshot = screen_capture(**SCREEN_POSITION_2)
        text = ocr(screenshot)
        type(text)

        time.sleep(1)
        keyboard.press_and_release('tab+enter')
        time.sleep(1)



if __name__ == "__main__":
    main()