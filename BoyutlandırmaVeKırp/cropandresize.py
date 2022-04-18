# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 12:52:01 2021

@author: Burak Atestepe
"""

import cv2

img = cv2.imread("homer.png")
cv2.imshow("Original",img)

resized = cv2.resize(img,(800,800))
#resized.shape width height
cv2.imshow("Resized",resized)

croped = img[:200,:300] #height,width
cv2.imshow("Cropped",croped)

cv2.waitKey(0)  # delay 0