#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 17:47:37 2018

@author: Richard Guinto
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt
import sys

filename = 'momandkids.jpg'
if len(sys.argv) > 1 :
    filename = sys.argv[1]


img = cv2.imread(filename)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
median5 = cv2.medianBlur(gray, 5)
 
blur = cv2.GaussianBlur(median5, (5,5),3)
sharp1 = cv2.addWeighted(median5, 1.5, blur, -0.5, 0)
 
median3 = cv2.medianBlur(gray, 3)
#plt.imshow(median3, cmap='gray')
#plt.show()
median33 = cv2.medianBlur(median3, 3)

blur = cv2.GaussianBlur(median33, (5,5),3)
sharp2 = cv2.addWeighted(median33, 1.5, blur, -0.5, 0)

#add text labels into each image to be displayed on screen
cv2.putText(sharp2,'(d) Sharpen double median filter 3x3', (10,20), cv2.FONT_HERSHEY_PLAIN, 1, (255,255,255))
cv2.putText(sharp1,'(c) Sharpen (b)', (10,20), cv2.FONT_HERSHEY_PLAIN, 1, (255,255,255))
cv2.putText(median5,'(b) with Median Filter 5x5', (10,20), cv2.FONT_HERSHEY_PLAIN, 1, (255,255,255))
cv2.putText(gray,'(a) Original', (10,20), cv2.FONT_HERSHEY_PLAIN, 1, (255,255,255))

#concatenate all images into 2x2 canvas
canvas1 = np.hstack([gray, median5])
canvas2 = np.hstack([sharp1, sharp2])
canvas = np.vstack([canvas1, canvas2])
 
cv2.imshow('press q to close', canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
