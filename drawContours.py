import numpy as np
from matplotlib import pyplot as plt
from cv2 import cv2
import time

def drawContours(image_original, image_thresh):
    image_contour, contours, hierarchy = cv2.findContours(image_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        # Skip if the contour area is small
        area = cv2.contourArea(cnt)
        if area < 500:
            continue
        # Draw the contour
        cv2.drawContours(image_original, [cnt], -1, (0, 255, 0), 2)
        # Find the center
        M = cv2.moments(cnt)
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        # Draw the center
        cv2.circle(image_original, (cX, cY), 3, (0, 0, 255), -1)