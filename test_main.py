import numpy as np
from matplotlib import pyplot as plt
from cv2 import cv2
import time

from color_filter import color_filter
from ROI import roi
from getTime import getTime
from resizeWithRatio import resize
from putText import putText
from drawLine import *
from drawContours import drawContours

#cap = cv2.VideoCapture("http://admin:SHTP_2020@192.168.1.100/cgi-bin/video.cgi?msubmenu=mjpg")
cap = cv2.VideoCapture('1.avi')

out = cv2.VideoWriter('result.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (1600, 900))

count = 0
states = "NG"
t = ""
time_capon = 0
time_capoff = 0


count_frame = 0

while(True):
    # Capture frame-by-frame
    ret, frame_from_cam = cap.read()

    # scale frame
    frame_scale = resize(frame_from_cam, 1600, 1200)

    # filter image
    frame_filter = color_filter(frame_scale)

    # select roi
    frame_roi = roi(frame_filter)
    
    count_frame = count_frame + 1

    if count_frame == 3:
        # draw contour from threshold image (frame_roi)
        count, states, t, time_capon, time_capoff = drawContours(frame_scale, frame_roi, count, states, t, time_capon, time_capoff)
        count_frame = 0

    putText(frame_scale, states, 1100, 650)
    putText(frame_scale, "Time: "+t, 1100, 700)
    putText(frame_scale, "Number of tests: " + str(count), 1100, 750)
    putText(frame_scale, "Number of OK: " + str(time_capon), 1100, 800)
    putText(frame_scale, "Number of NG: " + str(time_capoff), 1100, 850)
    out.write(frame_scale)
    

    cv2.imshow("frame", frame_scale)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()