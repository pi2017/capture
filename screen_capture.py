# Simple desktop recorder to *. avi
# Need to make directory /static
# Author: Oleksii Savchenko
# Date: 20/09/2019
# Usage python screen_capture.py
# pip install pyautogui

import cv2
import numpy as np
import os
import pyautogui

output = "static/desktop_video.avi"
img = pyautogui.screenshot()
img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
# get info from img
height, width, channels = img.shape
print('Frame: ', width, 'x', height)
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output, fourcc, 30.0, (width, height))
print ('Start saving Desktop...')

while True:
    try:
        img = pyautogui.screenshot()
        image = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        out.write(image)
        StopIteration(0.5)

    except KeyboardInterrupt:
        break

out.release()
cv2.destroyAllWindows()
