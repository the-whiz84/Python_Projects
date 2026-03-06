# Day 94 - Computer Vision + Input Automation for Game Bots

This project is a tiny game bot, but it introduces an important automation pattern: observe a small region of the screen, reduce it to a simple signal, and trigger input when that signal crosses a threshold.

The Dino game is just the sandbox. The real lesson is reactive automation driven by image data.

## 1. Watch a Small Part of the Screen, Not the Whole Desktop

The script begins by defining the dinosaur position and a bounding box in front of it:

```python
dino_coords = (2290, 1100)
box = (
    dino_coords[0] + 100,
    dino_coords[1],
    dino_coords[0] + 200,
    dino_coords[1] + 50,
)
```

That is a strong design choice. The bot does not need to analyze the full screen. It only needs the strip of pixels where obstacles will appear next.

Shrinking the observation window makes the loop cheaper and the detection logic simpler.

## 2. Turn the Screen Region into a Numeric Signal

The capture step uses `ImageGrab` and `ImageOps`:

```python
def capture_screen():
    image = ImageGrab.grab(box)
    gray_image = ImageOps.grayscale(image)
    return np.array(gray_image)
```

Converting to grayscale is important because the bot does not care about color. It only cares whether the visual intensity in that region suggests an obstacle.

The result is then reduced to a very simple test:

```python
def detect_obstacle(screen_data):
    return np.sum(screen_data) < 1000
```

This is primitive computer vision, but it is still computer vision. The code transforms an image into an array and then uses a threshold over the sum of pixel values as the trigger signal.

## 3. Convert Detection into Automated Input

Once an obstacle is detected, the bot simulates a jump:

```python
def jump():
    pyautogui.keyDown("space")
    time.sleep(0.05)
    pyautogui.keyUp("space")
```

That short press is enough to connect the perception layer to the control layer. This is the core loop of a bot:

- capture state
- interpret state
- send input

## 4. Run the Whole Bot as a Reactive Loop

The main loop is deliberately simple:

```python
def main():
    print("Starting in 3 seconds...")
    time.sleep(3)
    while True:
        screen_data = capture_screen()
        if detect_obstacle(screen_data):
            jump()
        time.sleep(0.1)
```

That short sleep prevents the loop from running as fast as possible all the time and gives the machine a brief pacing interval.

The main limitation of this project is also part of the lesson: the detection depends on hardcoded coordinates and a hardcoded threshold. That means the bot is tied to a specific resolution and game placement. For a first automation bot, that is acceptable. It is better to understand the perception-control loop clearly before generalizing it.

## How to Run the Dino Bot

1. Install the required packages if needed:
   ```bash
   pip install pyautogui pillow numpy
   ```
2. Position the Chrome Dino game so the hardcoded coordinates match your screen.
3. Run the script:
   ```bash
   python main.py
   ```
4. Verify the flow:
   - the script waits 3 seconds before starting
   - the capture region observes the area ahead of the dinosaur
   - the bot presses space when an obstacle enters that region

## Summary

Today, you built a simple vision-driven bot. The script captures a focused region of the screen, converts it into grayscale numeric data, uses a threshold to detect obstacles, and turns that detection into automated keyboard input. The larger idea is bigger than this game: many automation tools work by reducing complex visual input into a small decision signal and acting on it fast.
