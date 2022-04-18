# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 22:45:18 2021

@author: Burak Atestepe
"""

import cv2
import numpy as np

img = cv2.imread("kart.png")

cv2.imshow("Orjinal",img)

width = 400
height = 500

pts1 = np.float32([[230,1],[1,472],[540,150],[338,617]])
pts2 = np.float32([[0,0],[0,height],[width,0],[width,height]])

matrix = cv2.getPerspectiveTransform(pts1,pts2)

imgOutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("nihai",imgOutput)

cv2.waitKey(0)