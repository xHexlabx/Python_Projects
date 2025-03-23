import keyboard
import pygetwindow as gw
import win32gui
import win32con
import time
import pydirectinput

def activate_window_and_press(window_title: str, key: str, press_count: int = 1000):
    """Finds a window by title, forces it to the foreground, and presses a key repeatedly."""
    windows = gw.getWindowsWithTitle(window_title)

    if not windows:
        print(f"⚠️ Window '{window_title}' not found!")
        return False

    window = windows[0]
    hwnd = window._hWnd  # Get window handle

    # Force window to foreground (for full-screen games)
    win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)  # Restore if minimized
    win32gui.SetForegroundWindow(hwnd)  # Bring to front
    time.sleep(0.5)  # Allow time for focus

    print(f"✅ Activated '{window_title}' and pressing '{key}' {press_count} times...")

    for _ in range(press_count):
        pydirectinput.press(key)  # Press and release the key
        time.sleep(0.01)  # Short delay between presses

    print("✅ Done!")
    return True
