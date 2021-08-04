import time
import keyboard
import pyautogui
import cv2
import numpy as np
import mouse

'''
START EDITABLE PARAMETERS
'''
# color of target to aim for
target_color = (149, 195, 232)

# target of save score button
save_score_color = (255, 209, 84)

# minimum size (pretty arbitrary) to ensure contour is large enough
contour_size_threshold = 100

# button to start / stop program
start_button = "p"
'''
END EDITABLE PARAMETERS
'''

# flag that is set when program is done (all 30 targets clicked)
finished = False

def react(scrot):
    # check whether there is a save button visible, indicating that we are done with the challenge
    global finished
    save_score_mask = cv2.inRange(scrot, save_score_color, save_score_color)
    save_score_contours, _ = cv2.findContours(save_score_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    save_score_contours = sorted(save_score_contours, key=cv2.contourArea, reverse=True)
    if len(save_score_contours) > 0 and cv2.contourArea(save_score_contours[0]) > contour_size_threshold:
        finished = True
        return
    
    # finding target
    target_mask = cv2.inRange(scrot, target_color, target_color)
    target_contours, _ = cv2.findContours(target_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    target_contours = sorted(target_contours, key=cv2.contourArea, reverse=True)
    if len(target_contours) > 0 and cv2.contourArea(target_contours[0]) > contour_size_threshold:
        # move mouse and click target
        (x_min, y_min, box_width, box_height) = cv2.boundingRect(target_contours[0])
        mouse.move(x_min + box_width // 2, y_min + box_height // 2, absolute=True)
        mouse.click()
        
# start the program
while True:
    if keyboard.is_pressed(start_button):
        break
    
time.sleep(0.2)

# run program
while True:
    # kill program by pressing start_button (automatically ends when done)
    if keyboard.is_pressed(start_button) or finished:
        break
        
    # take screenshot and call function
    scrot = np.array(pyautogui.screenshot())
    react(scrot)
