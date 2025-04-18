import pyautogui
import keyboard
import math
import time

hotkey = 'l'

startX = 740
startY = 390

screen_width, screen_height = pyautogui.size()

screenMultiplierX = screen_width/1920
screenMultiplierY = screen_height/1080
tileW = math.ceil(63 * screenMultiplierX)
tileH = math.ceil(63 * screenMultiplierY)

x = math.ceil(startX * screenMultiplierX)
y = math.ceil(startY * screenMultiplierY)

x2 = math.ceil(810 * screenMultiplierX)
y2 = math.ceil(490 * screenMultiplierY)

x3 = math.ceil(940 * screenMultiplierX)
y3 = math.ceil(500 * screenMultiplierY)

x4 = math.ceil(1110 * screenMultiplierX)
y4 = math.ceil(590 * screenMultiplierY)

while True:
    print("Insert number of ammo: ")
    numberOfAmmo = int(input())
    print("Insert split size: ")
    splitSize = input()

    keyboard.wait(hotkey)

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
        pyautogui.moveTo(x + tileW * 2, y, 0.5)
        pyautogui.mouseDown()
        pyautogui.moveTo(x + tileW, y, 0.5)
        pyautogui.mouseUp()
        time.sleep(0.3)

        pyautogui.moveTo(x, y + tileH)
        pyautogui.click(button='right')
        pyautogui.moveTo(x2, y2 + tileH)
        pyautogui.click(button='left')
        pyautogui.moveTo(x3, y3)
        pyautogui.click(button='left')
        pyautogui.click(button='left')
        pyautogui.write(splitSize)
        pyautogui.moveTo(x4, y4)
        pyautogui.click(button='left')
        pyautogui.moveTo(x + tileW * 2, y, 0.5)
        pyautogui.mouseDown()
        pyautogui.moveTo(x + tileW, y, 0.5)
        pyautogui.mouseUp()
        time.sleep(0.3)
    
    pyautogui.moveTo(x, y)
    pyautogui.mouseDown()
    pyautogui.moveTo(x + tileW, y, 0.5)
    pyautogui.mouseUp()
    time.sleep(0.3)
    pyautogui.moveTo(x, y + tileH)
    pyautogui.mouseDown()
    pyautogui.moveTo(x + tileW, y, 0.5)
    pyautogui.mouseUp()
