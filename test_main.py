import numpy as np
from matplotlib import pyplot as plt
from cv2 import cv2

from color_filter import color_filter
from ROI import roi
from getTime import getTime
from resizeWithRatio import resize
from putText import putText


cap = cv2.VideoCapture('1.avi')

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # scale khung hình
    frame = resize(frame, 1600, 1200)
    frame = roi(frame)

    #plt.imshow(frame)
    #plt.show()
    frame = putText(frame, "OK")
    
    # Display the resulting frame
    cv2.imshow('Frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()