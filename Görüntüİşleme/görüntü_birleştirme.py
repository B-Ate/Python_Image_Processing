# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 15:20:08 2021

@author: Burak Atestepe
"""

import cv2
import numpy as np

img = cv2.imread("fenerbahce.png")

cv2.imshow("original",img)

hor = np.hstack((img,img))
cv2.imshow("yatay birleştirme",hor)

ver = np.vstack((img,img))
cv2.imshow("dikey birleştirme",ver)

cv2.waitKey(0)

