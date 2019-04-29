import cv2
import numpy as np
import matplotlib.pyplot as plt
import os, sys

OriginalImage = cv2.imread('hand.jpg',0)   # get the a gray-scale image
plt.figure(1)
plt.subplot(221),plt.imshow(OriginalImage,'gray')

GaussianImage = cv2.GaussianBlur(OriginalImage,(3,3),0)
plt.subplot(222),plt.imshow(GaussianImage,'gray')

ret,thrsh_GaussianImage =       cv2.threshold(GaussianImage,225,255,cv2.THRESH_BINARY)
plt.subplot(223),plt.imshow(thrsh_GaussianImage,'gray')
plt.show()

im, contours, hierarchy =     cv2.findContours(thrsh_GaussianImage,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(thrsh_GaussianImage,contours,-1,(0,255,0),3)
cv2.imshow("j", im)
cv2.waitKey()
