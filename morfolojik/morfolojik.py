# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 00:26:53 2021

@author: Burak Atestepe
"""

import cv2 
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("datai_team.jpg",0)
#img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(img, cmap = "gray"),plt.axis("off"),plt.title("original"),plt.show()

#erozyon

kernel = np.ones((5,5),dtype =np.uint8)
result = cv2.erode( img, kernel, iterations = 1)
plt.imshow(result, cmap = "gray"),plt.axis("off"),plt.title("erozyon"),plt.show()

#genişleme

result2 = cv2.dilate(img,kernel,iterations = 1)
plt.imshow(result2, cmap = "gray"),plt.axis("off"),plt.title("genişleme"),plt.show()

#whitenoise

whiteNoise = np.random.randint(0,2,size = img.shape[:2]) #only row col
whiteNoise = whiteNoise * 255
plt.imshow(whiteNoise, cmap = "gray"),plt.axis("off"),plt.title("whitenoise"),plt.show()

noise_img = whiteNoise + img
plt.imshow(noise_img, cmap = "gray"),plt.axis("off"),plt.title("whitenoise img"),plt.show()

#açılma

opening = cv2.morphologyEx(noise_img.astype(np.float32),cv2.MORPH_OPEN,kernel)
plt.imshow(opening, cmap = "gray"),plt.axis("off"),plt.title("opening img"),plt.show()


#kapatma

blackNoise = np.random.randint(0,2,size = img.shape[:2]) #only row col
blackNoise = whiteNoise * -255
plt.imshow(blackNoise, cmap = "gray"),plt.axis("off"),plt.title("blacknoise"),plt.show()

b_noise_img = blackNoise + img
b_noise_img[b_noise_img < -245] = 0
plt.imshow(b_noise_img, cmap = "gray"),plt.axis("off"),plt.title("b_noise_img"),plt.show()

closing = cv2.morphologyEx(noise_img.astype(np.float32),cv2.MORPH_CLOSE,kernel)
plt.imshow(closing, cmap = "gray"),plt.axis("off"),plt.title("closing img"),plt.show()

#•gradient
gradient = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)
plt.imshow(gradient, cmap = "gray"),plt.axis("off"),plt.title("gradient img"),plt.show()


cv2.waitKey(0)