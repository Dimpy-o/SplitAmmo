import pyautogui
import keyboard
import math
import time

numberOfAmmo = 0
splitSize = "0"

# Set the coordinates where you want to move and click
x = 1500
y = 750

x2 = 1550
y2 = 950

x3 = 1900
y3 = 1000

x4 = 2250
y4 = 1200

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