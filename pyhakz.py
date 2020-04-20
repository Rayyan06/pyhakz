import pyautogui
import time
import os
from PIL import ImageGrab
import numpy as np
import cv2
#import tensorflow as tf

#q_table = np.zeros([])

#MOVEMENT_SPEED = 1
NUMBER_OF_BULLETS = 1


EGG_PICTURE = 'egg.png'
PLAY_BUTTON = 'PLAY_BUTTON.png'
#PLAY_GAME = (1000, 500)


def screen_record():
    last_time = time.time()
    while True:
        # 800x600 windowed mode
        printscreen_pil =  ImageGrab.grab(bbox=(0,40,800,640))

        print('loop took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        #printscreen_numpy = np.array(printscreen_pillow.getdata(),dtype='uint8').reshape((printscreen_pillow.size[1],printscreen_pillow.size[0],3))
        #cv2.imshow('window',printscreen_numpy)
        #if cv2.waitKey(25) & 0xFF == ord('q'):
        #    cv2.destroyAllWindows()
        #    break


if __name__ =="__main__":
    screen_record()
