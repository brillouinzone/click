import pyautogui
import time

try:
    while True:
        pyautogui.click()  # Click the mouse
        time.sleep(1)      # Wait for 1 second
except KeyboardInterrupt:
    print("Script terminated by user.")