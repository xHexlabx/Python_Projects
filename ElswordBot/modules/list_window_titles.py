import pygetwindow as gw

def list_window_titles():
    """Lists all open window titles."""
    windows = gw.getAllWindows()
    for window in windows:
        if window.title:  # Filter out empty titles
            print(window.title)