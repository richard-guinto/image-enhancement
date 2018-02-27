#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 17:08:59 2018

@author: Richard Guinto
"""

import cv2
import sys

showpixel = False
window = 'Press q to close'
 
def display_pixel(event, x, y, flags, param):
    # grab references to the global variables
    global showpixel, image
 
    # if the left mouse button was clicked, start showing pixel info
    if event == cv2.EVENT_LBUTTONDOWN:
        showpixel = True
 
    elif event == cv2.EVENT_MOUSEMOVE:
        if showpixel == True:
            image = clone.copy()
            R = image[y,x,2]
            G = image[y,x,1]
            B = image[y,x,0]
            font = cv2.FONT_HERSHEY_PLAIN
            label = 'x:' + str(x) + ' y:' + str(y) + ' B:' + str(B) + ' G:' + str(G) + ' R:' + str(R)
            cv2.putText(image,label, (x,y), font, 1, (255 - int(B),255 - int(G),  255 - int(R)))
            cv2.imshow(window, image)


filename = 'RGB.png'
if len(sys.argv) > 1 :
    filename = sys.argv[1]
    
#image = cv2.imread('/Users/richard/MSEE/CS282/PA1/RGB.png', cv2.IMREAD_COLOR)
image = cv2.imread(filename, cv2.IMREAD_COLOR)




clone = image.copy()
cv2.startWindowThread()
cv2.namedWindow(window)
cv2.setMouseCallback(window, display_pixel)
 
# keep looping until the 'q' key is pressed
while True:
    # display the image and wait for a keypress
    cv2.imshow(window, image)
    key = cv2.waitKey(10) & 0xFF
 
    # if the 'q' key is pressed, break from the loop
    if key == ord("q"):
        break
 
# close all open windows
cv2.destroyAllWindows()