# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 17:05:53 2021

@author: Burak Atestepe
"""

import cv2 
import matplotlib.pyplot as plt

img = cv2.imread("sudoku.jpg",0)
plt.figure(), plt.imshow(img, cmap = "gray"), plt.axis("off"), plt.title("original"), plt.show()

# x gradyan yatay kenarları algılar
sobelx = cv2.Sobel(img,ddepth = cv2.CV_16S, dx =1 , dy = 0,ksize = 5)
plt.figure(), plt.imshow(sobelx, cmap = "gray"), plt.axis("off"), plt.title("sobelx"), plt.show()

# y gradyan dikey kenarları algılar
sobely = cv2.Sobel(img,ddepth = cv2.CV_16S, dx =0 , dy = 1,ksize = 5)
plt.figure(), plt.imshow(sobely, cmap = "gray"), plt.axis("off"), plt.title("sobely"), plt.show()

laplacian = cv2.Laplacian(img,ddepth = cv2.CV_16S)
plt.figure(), plt.imshow(laplacian, cmap = "gray"), plt.axis("off"), plt.title("laplacian   "), plt.show()