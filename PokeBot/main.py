import keyboard
import time
from PokeBot.modules import VS_Seekers , Battle


def main():
    print("PokeBot is running...🤖\nPress 'Enter' to continue...")

    # Wait until the 'Enter' key is pressed
    while not keyboard.is_pressed("\\"):
        pass

    print("PokeBot Activated !!!")

    # Run VS_Seekers, but allow stopping with "q"
    print("Press 'q' to stop VS_Seekers...")

    while not keyboard.is_pressed("q"):

        VS_Seekers()
        Battle()
        time.sleep(1)  # Small delay to prevent excessive CPU usage

    print("PokeBot Stopped!")

if __name__ == "__main__":
    main()
