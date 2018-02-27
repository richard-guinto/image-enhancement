#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 20:22:45 2018

@author: Richard Guinto
"""

import cv2
import matplotlib.pyplot as plt
import sys

filename = 'building.tif'
if len(sys.argv) > 1 :
    filename = sys.argv[1]

img = cv2.imread(filename)

blur = cv2.GaussianBlur(img, (5,5),3)
mask = img - blur
sharp1 = cv2.addWeighted(img, 1.5, blur, -0.5, 0)
sharp2 = cv2.addWeighted(img, 3.5, blur, -2.5, 0)
sharp3 = cv2.addWeighted(img, 5.5, blur, -4.5, 0)

plt.subplot(2,3,1)
plt.imshow(img)
plt.title('Original')
plt.xticks([]), plt.yticks([])

plt.subplot(2,3,2)
plt.imshow(blur)
plt.title('Gaussian Blur')
plt.xticks([]), plt.yticks([])

plt.subplot(2,3,3)
plt.imshow(mask)
plt.title('Mask')
plt.xticks([]), plt.yticks([])

plt.subplot(2,3,4)
plt.imshow(sharp1)
plt.title('Sharpen (1.5, -0.5)')
plt.xticks([]), plt.yticks([])

plt.subplot(2,3,5)
plt.imshow(sharp2)
plt.title('Sharpen (3.5, -2.5)')
plt.xticks([]), plt.yticks([])

plt.subplot(2,3,6)
plt.imshow(sharp3)
plt.title('Sharpen (5.5, -4.5)')
plt.xticks([]), plt.yticks([])

plt.show()