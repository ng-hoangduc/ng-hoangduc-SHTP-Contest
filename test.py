import numpy as np
from matplotlib import pyplot as plt
from cv2 import cv2
from color_filter import color_filter
from ROI import roi

# Read image
cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
img = cv2.imread('image/1.jpg')

# Lọc màu
#img = color_filter(img)
img = roi(img)
cv2.imshow('Image',img)



cv2.waitKey(0)
cv2.destroyAllWindows()