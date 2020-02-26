# Simple capture and XVID compress to *. avi
# Need to make directory /static
# Author: Oleksii Savchenko
# Date: 24/10/2020
# Usage python capture_xvid.py
# pip install numpy

import numpy as np
import cv2
import time

# Find OpenCV version
ver = (cv2.__version__)
print('CV2: ', format(ver))

fps = 30

output = 'static/web_output.avi'
cap = cv2.VideoCapture(0 + cv2.CAP_DSHOW)

v_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
          int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

# Define the codec and create VideoWriter object
# fourcc = cv2.VideoWriter_fourcc(*'X264')
# fourcc = cv2.VideoWriter_fourcc(*'DIVX')
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(output, fourcc, fps, v_size)

frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
              int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

print("IMAGE SIZE: ", frame_size)
print("FPS: ", cv2.CAP_PROP_FPS)
print('Press ESC to close window...')

prevTime = 0

while True:
    retval, frame = cap.read()
    if not retval:
        break

    curTime = time.time()
    sec = curTime - prevTime
    prevTime = curTime

    fps = 1 / (sec)

    str = "FPS : %0.1f" % fps

    cv2.putText(frame, str, (20, 460), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 240))

    cv2.imshow('WEB', frame)
    out.write(frame)

    key = cv2.waitKey(1)
    if (key == 27):
        print("Check /static for new file...")
        break

if cap.isOpened():
    cap.release()
    out.release()
    cv2.destroyAllWindows()
