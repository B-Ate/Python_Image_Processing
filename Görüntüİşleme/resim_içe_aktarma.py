# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 22:29:54 2021

@author: Burak Atestepe
"""


import cv2

## içe aktarma

resim = cv2.imread("fenerbahce.png",0)

## görselleştir

cv2.imshow("ilkresim",resim)
k = cv2.waitKey(0) & 0xFF

if(k == 27): #esc
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('fb.png',resim)
