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
#cv2.namedWindow('Image', cv2.WINDOW_NORMAL)

cap = cv2.VideoCapture('1.avi')

out = cv2.VideoWriter('result.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (1600, 900))

while(True):
    # Capture frame-by-frame
    ret, frame_from_cam = cap.read()

    # scale frame
    frame_scale = resize(frame_from_cam, 1600, 1200)

    # filter image
    frame_filter = color_filter(frame_scale)

    # select roi
    frame_roi = roi(frame_filter)
    
    # delay for low fps
    key = cv2.waitKey(50)
    
    # draw contour from threshold image (frame_roi)
    drawContours(frame_scale, frame_roi)
    #img=cv2.imread('Image_117.jpg')
    #rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    #hsv=cv2.cvtColor(rgb,cv2.COLOR_RGB2HSV_FULL)

    #plt.imshow(hsv)
    #plt.show()
    out.write(frame_scale)
    cv2.imshow("frame", frame_scale)
    # press z to pause
    if cv2.waitKey(1) & 0xFF == ord('z'):
        time.sleep(15)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()