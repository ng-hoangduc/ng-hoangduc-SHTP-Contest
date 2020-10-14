import numpy as np
from matplotlib import pyplot as plt
from cv2 import cv2
from getTime import getTime
import time
from putText import putText
from copy import copy


def drawContours(image_original, image_thresh, count, states, t, time_capon, time_capoff):
    image_contour, contours, hierarchy = cv2.findContours(image_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    print("Number of Contours found = " + str(len(contours))) 
    #putText(image_original, "Number of object: " + str(number_of_objects_in_image), 500, 350)
    for cnt in contours:
        # Skip if the contour area is small
        area = cv2.contourArea(cnt)
        
        if area < 700:
            continue

        # Draw the contour
        #cv2.drawContours(image_original, [cnt], -1, (0, 255, 0), 2)

        # Find the center
        M = cv2.moments(cnt)
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])


        if cX < 750 or cX > 875:
            continue

        rect = cv2.boundingRect(cnt)
        if rect[2]*rect[3] < 1000: 
            continue

        a,b,w,h = rect
        cv2.rectangle(image_original,(a,b),(a+w,b+h),(0,255,0),2)

        s = rect[2]*rect[3]
        
        # Draw the center
        cv2.circle(image_original, (cX, cY), 3, (0, 0, 255), -1)

        if s > 6000:
            count = count + 1
            states = "OK"
            t = getTime()
            time_capon = time_capon + 1
            #putText(image_original, "OK", 1000, 750)
            #putText(image_original, t, 1000, 800)
        
        if s < 4000:
            count = count + 1
            states = "NG"
            t = getTime()
            time_capoff = time_capoff + 1

            NG_image = image_original.copy()
            putText(NG_image, states, 1100, 650)
            putText(NG_image, "Time: "+t, 1100, 700)
            putText(NG_image, "Number of tests: " + str(count), 1100, 750)
            putText(NG_image, "Number of OK: " + str(time_capon), 1100, 800)
            putText(NG_image, "Number of NG: " + str(time_capoff), 1100, 850)
            name = './NG_' + str(time_capoff) + '.jpg'
            cv2.imwrite(name, NG_image) 
    
    return count, states, t, time_capon, time_capoff
        