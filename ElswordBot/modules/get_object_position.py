import pyautogui

def get_object_position(image_file: str, confidence: float = 0.3):
    """Find the object on the screen and return its center position."""
    try:
        position = pyautogui.locateCenterOnScreen(image_file, confidence=confidence)
        if position:
            return position  # Returns (x, y) coordinates
        else:
            return None  # Image not found
    except Exception as e:
        print(f"Error locating {image_file}: {e}")
        return None
