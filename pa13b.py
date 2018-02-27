#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 18:56:02 2018

@author: richard
"""

import numpy as np
import cv2
import sys

filename = 'cells27.jpg'
if len(sys.argv) > 1 :
    filename = sys.argv[1]

img = cv2.imread(filename)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
inv = 255 - gray

canvas = np.hstack([gray, inv])
cv2.imshow("Negative Transformation", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()

