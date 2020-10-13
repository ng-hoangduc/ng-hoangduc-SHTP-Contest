import numpy as np
from matplotlib import pyplot as plt
from cv2 import cv2
from color_filter import color_filter
from ROI import roi

# Read image
#cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
#img = cv2.imread('image/1.jpg')



# Lọc màu
#img = color_filter(img)
#img = roi(img)
#cv2.imshow('Image',img)

#cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.avi', fourcc, 10.0, (1920,1080))
#cap = cv2.VideoCapture("http://admin:SHTP_2020@192.168.1.100/cgi-bin/video.cgi?msubmenu=mjpg")
cap = cv2.VideoCapture("http://admin:SHTP_2020@192.168.0.107/cgi-bin/video.cgi?msubmenu=mjpg")
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame_width = frame.shape[0]
    frame_height = frame.shape[1]

    # Display the resulting frame
    cv2.imshow('Frame',frame)
    out.write(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()