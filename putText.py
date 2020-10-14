import numpy as np
from matplotlib import pyplot as plt
from cv2 import cv2

from color_filter import color_filter
from ROI import roi
from getTime import getTime
from resizeWithRatio import resize

def putText(image, text):
    # font 
    font = cv2.FONT_HERSHEY_SIMPLEX 
    # org 
    org = (1400, 800) 
    # fontScale 
    fontScale = 1.5
    # Blue color in BGR 
    color = (255, 0, 0) 
    # Line thickness of 2 px 
    thickness = 1
    # Using cv2.putText() method 
    image = cv2.putText(image, text, org, font, fontScale, color, thickness, cv2.LINE_AA) 
    return image