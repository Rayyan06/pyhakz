import pyautogui
import time
import os
from PIL import ImageGrab
import numpy as np
import cv2
from experiment import EggFinder

def process_img(image):
    processed_img = image
    return processed_img


    """# convert to gray
    processed_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # edge detection
    processed_img = cv2.Canny(processed_img, threshold1=200, threshold2=300)
    return processed_img"""

def main():
    last_time = time.time()
    eggfinder = EggFinder()
    while True:
        screen =  np.array(ImageGrab.grab(bbox=(0,40,800,640)))
        eggs = eggfinder.findEggs(screen)
        print(eggs)
        print('loop took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        new_screen = process_img(screen)
        #egg_loc = read_image(new_screen)
        #print(egg_loc)
        cv2.imshow('window',screen)
        #cv2.imshow('window', updateScreen(new_screen))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

main()

from IPython.display import Image
Image(filename='edge-detection.png')
