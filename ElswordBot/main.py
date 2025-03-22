import keyboard
from ultralytics import YOLO
from ElswordBot.modules import track_character, list_window_titles, activate_window_and_press


def main():
    """Initialize and run the Elsword Bot."""
    # model = YOLO('./models/best.pt')
    #
    # print("Elsword Bot is running... 🤖")
    # keyboard.wait("1")  # Wait for user to start
    # print("Tracking started!")
    #
    # track_character(model=model, delay=1.0)

    list_window_titles()
    activate_window_and_press(window_title="Saltfish" , key="k")

if __name__ == "__main__":
    main()
