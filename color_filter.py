import numpy as np
from matplotlib import pyplot as plt
from cv2 import cv2

def color_filter(image):
    """
    Lọc màu nắp chai:
    Chỉnh range của màu muốn lọc (lower, upper)
    ---> Vàng: lower(20,100 ,100), upper(40, 255, 255)
    ---> Xanh dương:lower(100, 150, 0), upper(140, 255, 255)

    lower_white = np.array([0,0,0], dtype=np.uint8)
    upper_white = np.array([0,0,255], dtype=np.uint8)
    
    Phép and để trả về ảnh màu ban đầu (not HSV) - ko and sẽ trả về ảnh binary
    """
    rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    hsv=cv2.cvtColor(rgb,cv2.COLOR_RGB2HSV_FULL)
    lower = np.array([65,60,60])
    upper = np.array([75,170,170])
    mask = cv2.inRange(hsv, lower, upper)
    masked = cv2.bitwise_and(hsv, hsv, mask = mask)
    masked = cv2.cvtColor(masked, cv2.COLOR_BGR2GRAY)
    masked = cv2.threshold(masked, 95, 255, cv2.THRESH_BINARY)[1]
    #masked = cv2.adaptiveThreshold(masked, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 15, 2)
    masked = cv2.medianBlur(masked, 7)
    return masked