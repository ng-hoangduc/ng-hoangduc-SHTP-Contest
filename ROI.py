import numpy as np
from matplotlib import pyplot as plt
from cv2 import cv2

def roi(img):
    """
    Lấy ROI của ảnh:
    Ảnh có kích thước (x, y) - (width, height)
    ROI là hình chữ nhật 4 points a, b, c, d:
        - a là điểm bên trái phía dưới
        - b là điểm bên phải phía dưới
        - c là điểm bên phải phía trên
        - d là điểm bên trái phía trên
    shape là array chứa 4 điểm HCN(a, b, c, d) - kích thước của ROI

    muốn tìm a, b, c, d dùng matplotlib sẽ show ảnh với tọa độ điểm trên ảnh:
        plt.imshow(image)
        plt.show()
    """
    x = int(img.shape[1])
    y = int(img.shape[0])
    shape = np.array([[int(0), int(170)], [int(1600), int(170)], [int(1600), int(0)], [int(0), int(0)]])

    #define a numpy array with the dimensions of img, but comprised of zeros
    mask = np.zeros_like(img)
    #Uses 3 channels or 1 channel for color depending on input image
    if len(img.shape) > 2:
        channel_count = img.shape[2]
        ignore_mask_color = (255,) * channel_count
    else:
        ignore_mask_color = 255
    #creates a polygon with the mask color
    cv2.fillPoly(mask, np.int32([shape]), ignore_mask_color)
    #returns the image only where the mask pixels are not zero
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image