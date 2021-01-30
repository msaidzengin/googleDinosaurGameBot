from PIL import ImageGrab, ImageOps
import pyautogui
import time

start_time = time.time()

while True:

    pass_time = int(time.time() - start_time)
    
    if pass_time > 55:
        cactus = ImageGrab.grab((550, 910, 570, 920))
        cactusColor = sum(Ima geOps.grayscale(cactus).getcolors()[0])

    elif pass_time > 25:
        cactus = ImageGrab.grab((500, 910, 520, 920))
        cactusColor = sum(ImageOps.grayscale(cactus).getcolors()[0])

    else:
        cactus = ImageGrab.grab((460, 910, 480, 920))
        cactusColor = sum(ImageOps.grayscale(cactus).getcolors()[0])

    
    if cactusColor != 455:
        print(cactusColor)
        pyautogui.press('space')
