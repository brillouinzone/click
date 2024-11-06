import pyautogui
import time
import threading
import numpy as np
import keyboard  # Requires the keyboard library to detect key press
import matplotlib.pyplot as plt

# Variables to hold the target coordinates
target_x, target_y = None, None

width, height = 100, 100  # Adjust as needed

screenshot_target = None
screenshot_test = None

def screenshot_at_position():
    top_left_x = target_x - width // 2
    top_left_y = target_y - height // 2

    # Capture the screenshot around the cursor
    screenshot = pyautogui.screenshot(region=(top_left_x, top_left_y, width, height))
    return screenshot

def set_target_position():
    global target_x, target_y
    # Capture the current mouse position as the target location
    target_x, target_y = pyautogui.position()
    print(f"Target position set to: ({target_x}, {target_y})")
    # Define the top-left corner of the area to capture


    # Convert the screenshot to a NumPy array
    screenshot_target = np.array(screenshot_at_position())
    plt.figure()
    plt.imshow(screenshot_target)
    plt.title("target")
    plt.show()


def virtual_click():
    while True:
        if target_x is not None and target_y is not None:
            screenshot_test = np.array(screenshot_at_position())
            plt.figure()
            plt.imshow(screenshot_test)
            plt.title("test")
            plt.show()


            # Click at the specified location

            pyautogui.click(target_x, target_y)
            print(f"Virtual click performed at ({target_x}, {target_y})")

        # Wait for 1 second before the next click
        time.sleep(2.)


# Start the virtual click function in a separate thread
click_thread = threading.Thread(target=virtual_click)
click_thread.daemon = True  # Daemon thread will exit when the main program exits
click_thread.start()

# Instructions to set the target area
print("Move the mouse to the target area and press 's' to set the click position.")

try:
    while True:
        # Check if the 's' key is pressed to set the target position
        if keyboard.is_pressed('s'):
            set_target_position()
            time.sleep(0.5)  # Small delay to prevent multiple detections
        time.sleep(0.1)  # Keep the main loop active
except KeyboardInterrupt:
    print("Program terminated.")