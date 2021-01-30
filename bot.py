from PIL import ImageGrab, ImageOps
import pyautogui
import time

while True:
    cactus = ImageGrab.grab((460, 910, 480, 920)) # Cactus coordinates can be changed.
    cactusColor = sum(ImageOps.grayscale(cactus).getcolors()[0])
    
    if cactusColor != 455:
        pyautogui.press('space')
