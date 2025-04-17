import pyautogui
import math
import time

numberOfAmmo = 0
splitSize = "0"

screen_width, screen_height = pyautogui.size()

# Set the coordinates where you want to move and click
x = math.ceil(750 * (screen_width/1920))
y = math.ceil(375 * (screen_height/1080))

x2 = math.ceil(775 * (screen_width/1920))
y2 = math.ceil(475 * (screen_height/1080))

x3 = math.ceil(950 * (screen_width/1920))
y3 = math.ceil(500 * (screen_height/1080))

x4 = math.ceil(1125 * (screen_width/1920))
y4 = math.ceil(600 * (screen_height/1080))

while True:
    print("Insert number of ammo: ")
    numberOfAmmo = int(input())
    print("Insert split size: ")
    splitSize = input()
    for i in range (0, math.ceil(numberOfAmmo / int(splitSize)) - 1):
        pyautogui.moveTo(x, y)
        pyautogui.click(button='right')
        pyautogui.moveTo(x2, y2)
        pyautogui.click(button='left')
        pyautogui.moveTo(x3, y3)
        pyautogui.click(button='left')
        pyautogui.click(button='left')
        pyautogui.write(splitSize)
        pyautogui.moveTo(x4, y4)
        pyautogui.click(button='left')
        time.sleep(0.4)
