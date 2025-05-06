import pyautogui as pt
import time
import keyboard

message = "Legend"
time.sleep(5)
for i in range(10):
    if keyboard.is_pressed('s'):
        break

    pt.write(f"{message}({i+1})")
    time.sleep(0.1)
    pt.press("enter")
    time.sleep(0.5)