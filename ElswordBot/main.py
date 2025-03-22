import keyboard
from ultralytics import YOLO
from ElswordBot.modules import track_character

def main():
    """Initialize and run the Elsword Bot."""
    model = YOLO('./models/best.pt')

    print("Elsword Bot is running... 🤖")
    keyboard.wait("1")  # Wait for user to start
    print("Tracking started!")

    track_character(model=model, delay=1.0)

if __name__ == "__main__":
    main()
