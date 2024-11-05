import pyautogui
import time
import threading
import keyboard  # Requires the keyboard library to detect key press

# Variables to hold the target coordinates
target_x, target_y = None, None


def set_target_position():
    global target_x, target_y
    # Capture the current mouse position as the target location
    target_x, target_y = pyautogui.position()
    print(f"Target position set to: ({target_x}, {target_y})")


def virtual_click():
    while True:
        if target_x is not None and target_y is not None:
            # Click at the specified location
            pyautogui.click(target_x, target_y)
            print(f"Virtual click performed at ({target_x}, {target_y})")

        # Wait for 1 second before the next click
        time.sleep(1.)


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