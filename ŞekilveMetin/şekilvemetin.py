# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 14:56:25 2021

@author: Burak Atestepe
"""

import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8) #siyah bir resims 1,1 olsaydı beyaz olurdu

print(img.shape)

cv2.imshow("Siyah",img)

#çizgi
cv2.line(img,(0,0),(512,512),(0,255,0),3) # (resim,başlangıç noktası,bitiş noktası, renk BGR, kalınlık)

cv2.imshow("Cizgi",img)


#dikdörtgen

cv2.rectangle(img,(0,0),(256,256),(255,0,0),cv2.FILLED) #cv2.Fılled ile içini doldurabiliyoruz

cv2.imshow("Dikdortgen",img)

#çember

cv2.circle(img,(300,300),45,(0,0,255)) #  (resim,merkez,yarı çap,renk)  

cv2.imshow("Cember",img)

#metin
#( resim, başlangıç noktası, font , kalınlık , renk)
cv2.putText(img,"Resim",(350,350),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255))

cv2.imshow("Metin",img)

cv2.waitKey(0)