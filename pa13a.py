#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 02:19:40 2018

@author: richard
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 19:03:56 2018

@author: Richard Guinto
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np
import sys

filename = 'dental.jpg'
if len(sys.argv) > 1 :
    filename = sys.argv[1]

img = cv2.imread(filename)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

plt.subplot(2,2,1),plt.imshow(gray,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])

im = gray/255.0
gamma = 0.6
power_law = cv2.pow(im, 1/gamma)
plt.subplot(2,2,2),plt.imshow(power_law,cmap = 'gray')
plt.title('gamma = ' + str(gamma)), plt.xticks([]), plt.yticks([])

gamma = 2.0
power_law = cv2.pow(im, 1/gamma)
plt.subplot(2,2,3),plt.imshow(power_law,cmap = 'gray')
plt.title('gamma = ' + str(gamma)), plt.xticks([]), plt.yticks([])

gamma = 2.5
power_law = cv2.pow(im, 1/gamma)
plt.subplot(2,2,4),plt.imshow(power_law,cmap = 'gray')
plt.title('gamma = ' + str(gamma)), plt.xticks([]), plt.yticks([])


plt.show()
  
 
