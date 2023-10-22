import pyautogui
import time
import pyscreeze

print("""
Welcome to AFK-ing tool for Shotgun Farmers
Hopefully you have read the documentation provided on GitHub
If not please put your game to resolution 1280x768 and turn off fullscreen mode

Script will start working by itself in 3 seconds
Enjoy using this afk tool :)
""")

time.sleep(5)

pyautogui.click(495, 777)
time.sleep(0.5)
pyautogui.click(529, 532)

while True:
    if pyautogui.pixel(700, 425)[0] == 12 or pyautogui.pixel(700, 425)[0] == 13 or pyautogui.pixel(1000, 730)[0] == 207:
        pyautogui.click(700, 425)
        pyautogui.click(1120, 425)
        pyautogui.click(1000, 730)
    else:
        for i in range(10):
            pyautogui.press("w")
        for i in range(10):
            pyautogui.press("a")
        for i in range(10):
            pyautogui.press("s")
        for i in range(10):
            pyautogui.press("d")


