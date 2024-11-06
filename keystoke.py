import pyautogui
import time

# Give a short delay before execution to switch to the target window
time.sleep(2)


while True:
    # Press CTRL + ALT + .
    pyautogui.hotkey('ctrl', 'alt', '.')
    print("ctrl+alt+.")
    time.sleep(1)