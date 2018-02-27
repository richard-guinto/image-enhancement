#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 10:39:38 2018

@author: richard
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt
import sys

filename = 'cameraman'
if len(sys.argv) > 1 :
    filename = sys.argv[1]


for i in range(1,5):
    img = cv2.imread(filename + str(i) + '.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    dft = cv2.dft(np.float32(gray),flags = cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)
    
    mag,angle = cv2.cartToPolar(dft_shift[:,:,0], dft_shift[:,:,1])
    
    mag_spectrum = 20*np.log(mag)
    
    plt.subplot(3,4, i)
    plt.imshow(gray, cmap='gray')
    plt.title('Image: ' + str(i))
    plt.xticks([]), plt.yticks([])
    
    plt.subplot(3,4, 4+i)
    plt.imshow(mag_spectrum, cmap='gray')
    plt.title('Magnitude ' + str(i))
    plt.xticks([]), plt.yticks([])

    plt.subplot(3,4, 8+i)
    plt.imshow(angle, cmap='gray')
    plt.title('Phase ' + str(i))
    plt.xticks([]), plt.yticks([])

plt.show()