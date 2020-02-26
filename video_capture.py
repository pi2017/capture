"""
Video Capture
Data:
Release:
"""

import cv2

# Find OpenCV version
ver = (cv2.__version__)
print('CV2: ', format(ver))

# function video capture
cameraCapture = cv2.VideoCapture(0 + cv2.CAP_DSHOW)
# rame rate or frames per second
fps = 30
video_sec = 20

# Width and height of the frames in the video stream
size = (int(cameraCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(cameraCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))

"""
Create a VideoWriter object. We should specify the output file name (eg: MyOutput.avi). 
Then we should specify the FourCC. Then number of frames per second (fps) and frame size should be passed. 
May specify isColor flag. If it is True, encoder expect color frame, otherwise it works with grayscale frame.
FourCC is a 4-byte code used to specify the video codec. The list of available codes can be found in fourcc.org. 
It is platform dependent.
==============================================================================================================
cv2.VideoWriter_fourcc(‘I’,’4’,’2’,’0’): This option is an uncompressed YUV encoding, 4:2:0 chroma subsampled. 
This encoding is widely compatible but produces large files. The file extension should be .avi.
cv2.VideoWriter_fourcc(‘P’,’I’,’M’,’1’): This option is MPEG-1 The file extension should be .avi.
cv2.VideoWriter_fourcc(‘X’,’V’,’I’,’D’): This option is MPEG-4 and a preferred option if you want 
the resulting video size to be average. The file extension should be .avi.
cv2.VideoWriter_fourcc(‘T’,’H’,’E’,’O’): This option is Ogg Vorbis. The file extension should be .ogv.
cv2.VideoWriter_fourcc(‘F’,’L’,’V’,’1’): This option is a Flash video. The file extension should be .flv.
cv2.VideoWriter_fourcc(‘U’,’2’,’6’,’3’): H263 codec
cv2.VideoWriter_fourcc(‘I’,’2’,’6’,’3’): H263I codec
cv2.VideoWriter_fourcc(‘D’,’I’,’V’,’X’): MPEG-4 codec
cv2.VideoWriter_fourcc(‘M’,’P’,’4’,’2’): MPEG-4.2 codec
cv2.VideoWriter_fourcc(‘D’,’I’,’V’,’3’): MPEG-4.3 codec
"""

videoWriter = cv2.VideoWriter('static/My_Output.avi',
                              cv2.VideoWriter_fourcc('X', 'V', 'I', 'D'), fps, size)

success, frame = cameraCapture.read()
print("Saving frames from camera...")

# some variable
numFramesRemaining = video_sec * fps - 1

# loop until there are no more frames and variable > 0
while success and numFramesRemaining > 0:
    videoWriter.write(frame)
    success, frame = cameraCapture.read()
    cv2.imshow('VideoStream', frame)
    cv2.waitKey(1)
    numFramesRemaining -= 1

# Closes video file or capturing device
cameraCapture.release()
