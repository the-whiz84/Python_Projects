import pyautogui
from PIL import ImageGrab, ImageOps
import time
import numpy as np

# Coordinates for the game window and dinosaur position
# These values need to be adjusted based on your screen resolution and game window position
dino_coords = (2290, 1100)  # Example coordinates for the dinosaur
box = (
    dino_coords[0] + 100,
    dino_coords[1],
    dino_coords[0] + 200,
    dino_coords[1] + 50,
)  # Area to detect obstacles


def capture_screen():
    image = ImageGrab.grab(box)
    gray_image = ImageOps.grayscale(image)
    return np.array(gray_image)


def detect_obstacle(screen_data):
    # Sum of pixel values to detect obstacles
    return np.sum(screen_data) < 1000  # Threshold value to detect obstacles


def jump():
    pyautogui.keyDown("space")
    time.sleep(0.05)
    pyautogui.keyUp("space")


def main():
    print("Starting in 3 seconds...")
    time.sleep(3)
    while True:
        screen_data = capture_screen()
        if detect_obstacle(screen_data):
            jump()
        time.sleep(0.1)  # Adjust the sleep time as needed


if __name__ == "__main__":
    main()
