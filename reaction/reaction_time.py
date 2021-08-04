import time
import keyboard
import pyautogui
import cv2
import numpy as np
import mouse

'''
START EDITABLE PARAMETERS
'''
# color of green rectangle
green = (75, 219, 106)

# minimum size (pretty arbitrary) to ensure contour is large enough
contour_size_threshold = 100

# button to start and stop program
start_button = "p"
'''
END EDITABLE PARAMETERS
'''


def react(scrot):
    # try to find contour that has specific green shade
    mask = cv2.inRange(scrot, green, green)
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    if len(contours) > 0 and cv2.contourArea(contours[0]) > contour_size_threshold:
        # react
        mouse.click()
        
        # wait a little
        time.sleep(1)
        
        # start the next round (there are 5 total)
        mouse.click()
        
# start the program
while True:
    if keyboard.is_pressed(start_button):
        break
    
time.sleep(0.2)

# run program
while True:
    # kill program by pressing start_button
    if keyboard.is_pressed(start_button):
        break
    
    # take screenshot and call function
    scrot = np.array(pyautogui.screenshot())
    react(scrot)
