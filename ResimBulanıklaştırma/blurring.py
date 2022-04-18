# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 00:44:42 2021

@author: Burak Atestepe
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

#blurring detayı azaltır,gürültüyü engeller

img = cv2.imread("NYC.jpg")
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.figure()
plt.imshow(img),plt.axis("off"),plt.title("original"),plt.show()

#ortalama bulanıklık 3e3 matrisin ortalamasını hesaplar

dst =cv2.blur(img,ksize = (3,3))
plt.figure(),plt.imshow(dst),plt.axis("off"),plt.title("ortalama Blur")

#gaussian blur

gb =cv2.GaussianBlur(img,ksize = (3,3), sigmaX = 7)
plt.figure(),plt.imshow(gb),plt.axis("off"),plt.title("gauss Blur")

#median blur 3e3 ü sıralar ortadakini alır
 
mb =cv2.medianBlur(img,ksize = 3)
plt.figure(),plt.imshow(mb),plt.axis("off"),plt.title("median Blur")

def gaussianNoise(image):
    row,col,ch = image.shape  #(543, 543, 3)
    mean = 0
    var = 0.05
    sigma = var **0.5
    
    gauss = np.random.normal(mean,sigma,(row,col,ch))
    gauss = gauss.reshape(row,col,ch)
    noisy  = image + gauss
    
    return noisy

#içe aktar normalize et

img = cv2.imread("NYC.jpg")
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)/255
plt.figure(),plt.imshow(img),plt.axis("off"),plt.title("original"),plt.show()

gaussianNoisyImage = gaussianNoise(img)
plt.figure(),plt.imshow(gaussianNoisyImage),plt.axis("off"),plt.title("Gaussian Noisy")

#gaussian blur
gb2 = cv2.GaussianBlur(gaussianNoisyImage,ksize =(3,3),sigmaX = 7)
plt.figure(),plt.imshow(gb2),plt.axis("off"),plt.title("Gaussian Blur")


def saltPepperNoise(image):
    row,col,ch = image.shape
    s_vs_p = 0.5
    
    amount = 0.004
    
    noisy = np.copy(image)
    
    #salt - beyaz noktacık
    num_salt = np.ceil(amount * image.size * s_vs_p) #ondalıklı sayı yukarı aşağı yuvarla
    coords = [np.random.randint(0,i-1,int(num_salt)) for i in image.shape]
    noisy[coords] = 1
    
    #pepper siyah
    num_papper = np.ceil(amount * image.size * 1-s_vs_p) #ondalıklı sayı yukarı aşağı yuvarla
    coords = [np.random.randint(0,i-1, int(num_papper)) for i in image.shape]
    noisy[coords] = 0
    
    return noisy


spImage = saltPepperNoise(img)
plt.figure(),plt.imshow(spImage),plt.axis("off"),plt.title("spImage")

mb2 =cv2.medianBlur(spImage.astype(np.float32),ksize = 3)
plt.figure(),plt.imshow(mb2),plt.axis("off"),plt.title(" with median Blur")



cv2.waitKey(0)