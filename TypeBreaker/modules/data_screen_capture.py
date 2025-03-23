import pyautogui
import time
import os
from datetime import datetime

def data_screen_capture(x1: int, y1: int, x2: int, y2: int,interval_seconds: int = 1, output_folder : str = "") -> None:

    width = x2 - x1
    height = y2 - y1

    cnt = 0

    try:
        while True:
            cnt += 1
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            file_path = os.path.join(output_folder, f"screenshot_{timestamp}.png")

            screenshot = pyautogui.screenshot(region=(x1, y1, width, height))
            screenshot.save(file_path)

            print(f"Saved: {file_path}")

            time.sleep(interval_seconds)
            pyautogui.click()
            time.sleep(interval_seconds)

            if cnt == 1000 : break

    except KeyboardInterrupt:
        print("\nScreen capture stopped.")