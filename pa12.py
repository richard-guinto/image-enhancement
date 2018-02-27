#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 17:08:59 2018

@author: richard
"""

import numpy as np
import cv2

cap = cv2.VideoCapture(0)
width = cap.get(3)/4
height = cap.get(4)/4

width = int(width)
height = int(height)

print('width: %d height: %d' % (width,height))
cap.set(3, width)
cap.set(4, height)
sigma = 0.33

while(True):
    ret, frame = cap.read()
  
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray3 = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    #gaussian = cv2.GaussianBlur(gray, (5,5),1)
    median = np.median(gray)
    lower = int (max(0, (1.0 - sigma) * median))
    upper = int (max(255, (1.0 - sigma) * median))
    edge = cv2.Canny(gray, lower, upper)
    edge3 = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR)
    cv2.putText(frame,'Original', (10,20), cv2.FONT_HERSHEY_PLAIN, 1, (255,255,255))
    cv2.putText(gray3,'Gray', (10,20), cv2.FONT_HERSHEY_PLAIN, 1, (255,255,255))
    cv2.putText(edge3,'Canny', (10,20), cv2.FONT_HERSHEY_PLAIN, 1, (255,255,255))
    canvas3 = np.hstack([frame, gray3, edge3])

    cv2.imshow('Press q to quit',canvas3)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
