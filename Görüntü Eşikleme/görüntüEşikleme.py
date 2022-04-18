# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 01:03:17 2021

@author: Burak Atestepe
"""

import cv2
import matplotlib.pyplot as plt


img = cv2.imread("img1.jpg")
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

plt.figure()
plt.imshow(img, cmap="gray")
plt.axis("off") #eksenleri kapatma
plt.show()

#eşikleme 60 üzerini beyazlayacak, 2 parametre döndüğü için başta _ işareti var bizim için önemi yok
#THRESH_BINARY_INV (60 üzerini siyah) ve THRESH_BINARY(60 üzerini beyaz) 

_,thresh_img = cv2.threshold(img,thresh = 60,maxval = 255,type =cv2.THRESH_BINARY_INV )

plt.figure()
plt.imshow(thresh_img, cmap="gray")
plt.axis("off") #eksenleri kapatma
plt.show()

#uyarlamalı eşik değeri
thresh_img2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,8)
plt.figure()
plt.imshow(thresh_img2, cmap="gray")
plt.axis("off") #eksenleri kapatma
plt.show()

cv2.waitKey(0)