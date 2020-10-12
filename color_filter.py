import numpy as np
from matplotlib import pyplot as plt
from cv2 import cv2

def color_filter(image):
    """
    Lọc màu nắp chai:
    Chỉnh range của màu muốn lọc (lower, upper)
    ---> Vàng: lower(20,100 ,100), upper(40, 255, 255)
    ---> Xanh dương:lower(100, 150, 0), upper(140, 255, 255)
    Phép and để trả về ảnh màu ban đầu (not HSV) - ko and sẽ trả về ảnh binary
    """
    rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    hls=cv2.cvtColor(rgb,cv2.COLOR_RGB2HSV_FULL)
    lower = np.array([20,100,100])
    upper = np.array([40,255,255])
    mask = cv2.inRange(hls, lower, upper)
    masked = cv2.bitwise_and(image, image, mask = mask)
    return masked