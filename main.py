import time

import cv2
import mss
import numpy as np
from pynput.keyboard import Key, Controller

keyboard = Controller()

def pressSpace():
    # print("JUMP!")
    keyboard.press(Key.space)
    time.sleep(.2)
    keyboard.release(Key.space)

def collision(y, x1, x2, x3):
    w1 = img.item(y,x1,0) != 255
    b1 = img.item(y,x1,0) != 36
    
    w2 = img.item(y,x2,0) != 255
    b2 = img.item(y,x2,0) != 36

    
    w3 = img.item(y,x3,0) != 255
    b3 = img.item(y,x3,0) != 36
    return ((w1 & b1) or (w2 & b2) or (w3 & b3))

with mss.mss() as sct:
    x = 49
    y = 0
    y2 = 99

    # Area to look on monitor (currently set on second monitor)
    mon = {'top': sct.monitors[2]["top"]+600, 'left': sct.monitors[2]["left"]+320, 'width': 50, 'height': 100, 'mon': 2}

    while 1:
        # last_time = time.time()

        # Get raw pixels from the screen
        # print(sct.grab(mon).size)
        img = np.array(sct.grab(mon)) # x, y, pixel (r, g, b, a)
        # pixel = img[y, x]
        img = cv2.circle(img,(x,y), 4, (0,255,0), 2)
        img = cv2.circle(img,(x,y2), 4, (255,0,0), 2)

        # print(f"1: {img.item(y,x,0)}")
        # print(f"2: {img.item(y2,x,0)}")

        # checks for greater than default black val
        #                              b   g   r    a
        # isBlack = np.greater(np.array([36, 33, 32, 255]), pixel)
        # isBlack = isBlack[0] & isBlack[1] & isBlack[2]
        # isBlack = img.item(y,x,0) > 36
        
        # checks for less than  white
        # isWhite = np.less(pixel, np.array([255, 255, 255, 255]))
        # isWhite = isWhite[0] & isWhite[1] & isWhite[2]
        # isWhite = img.item(y,x,0) < 255
        
        # isBlack = img.item(y,x,0) != 36
        col = collision(y, x, x-1, x-2)
        col2 = collision(y2, x, x-1, x-2)
        
        # print(f"1: {col}; 2: {col2}")

        if col or col2:
            pressSpace()
            pass
            
        # Display the image
        cv2.imshow('Dino', img)
        # print(f"fps: {1/(time.time()-last_time)}")

        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break