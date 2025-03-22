import pyautogui
import pygetwindow as gw
import time

def activate_window_and_press(window_title: str, key: str):
    """Finds a window by title, activates it, and presses a key."""
    windows = gw.getWindowsWithTitle(window_title)

    if not windows:
        print(f"⚠️ Window '{window_title}' not found!")
        return False

    window = windows[0]
    window.activate()  # Activate the window
    time.sleep(0.2)  # Give it time to focus

    pyautogui.press(key)  # Press the key

    print(f"✅ Pressed '{key}' in '{window_title}'")
    return True

# Example Usage
activate_window_and_press("Elsword", "space")  # Change window title & key as needed
