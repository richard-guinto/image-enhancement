#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 19:00:28 2018

@author: Richard Guinto
"""

import numpy as np
import cv2
#import matplotlib.pyplot as plt
import sys

filename = 'butterfly.jpg'
if len(sys.argv) > 1 :
    filename = sys.argv[1]

img = cv2.imread(filename)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#perform median filter to remove the salt and pepper noise
median = cv2.medianBlur(gray, 3)
#concatenate original image and the enhanced image
canvas = np.hstack([gray, median])

#compute the histogram of the enhanced image
hist1 = cv2.calcHist([median],[0],None,[256],[0,256])

#perform automatic histogram equalization and append to the output window
medianeq = cv2.equalizeHist(median)
canvas = np.hstack([canvas, medianeq])

hist2 = cv2.calcHist([medianeq],[0],None,[256],[0,256])

# enable this three lines if you want to display the histogram
#plt.plot(hist1)
#plt.plot(hist2)
#plt.show()
 
cv2.imshow('press q to close the window', canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
 
