import pyautogui
import keyboard
import time

# Wait 3 seconds before starting to press the "F" key
time.sleep(3)

print("Holding 'F' pressed. Press 'G' to stop.")

def hold_f_pressed():
    pyautogui.keyDown('f')  # Press and hold "F" without releasing
    while True:
        if keyboard.is_pressed('g'):  # If "G" is pressed, release "F"
            pyautogui.keyUp('f')  # Release the "F" key
            print("Stopped.")
            break
        time.sleep(0.1)  # This sleep is to not overload the loop with the check

try:
    hold_f_pressed()
except KeyboardInterrupt:
    pyautogui.keyUp('f')  # Ensure the "F" key is released if the script is manually stopped
    print("Script manually stopped.")
