# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 00:04:40 2022

@author: Burak Atestepe
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("sudoku.jpg", 0)
img = np.float32(img) #ondalıklı sayıya dönştürülüyor
plt.figure(), plt.imshow(img, cmap="gray"), plt.axis("off")

#harris corner detection

dst = cv2.cornerHarris(img, blockSize = 2, ksize = 3, k = 0.04)
plt.figure(), plt.imshow(dst, cmap="gray"), plt.axis("off")

dst = cv2.dilate(dst, None) #genişletme tespit ettğin noktaları genişlet
img[dst>0.2*dst.max()] = 1
plt.figure(), plt.imshow(dst, cmap="gray"), plt.axis("off")

#shi tomsai detection

img = cv2.imread("sudoku.jpg", 0)
img = np.float32(img)
corners = cv2.goodFeaturesToTrack(img, 100, 0.01, 10)
corners = np.int64(corners)

for i in corners:
    x,y = i.ravel()
    cv2.circle(img, (x,y),3,(125,125,125),cv2.FILLED)

plt.figure(), plt.imshow(img, cmap="gray"), plt.axis("off")


