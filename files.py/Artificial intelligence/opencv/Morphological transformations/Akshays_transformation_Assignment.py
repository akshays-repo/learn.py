#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 13:30:21 2020

@author: akshays
"""

import cv2
import numpy as np

img = cv2.imread('/home/akshays/programs/learn.py/files.py/Artificial intelligence/opencv/Morphological transformations/AI.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

kernel = np.ones((11,11),np.uint8)

erosion = cv2.erode(img,kernel,iterations = 1)
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
dilation = cv2.dilate(img,kernel,iterations = 1)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)


cv2.imshow('orginal',img)
cv2.imshow('erosion',erosion)
cv2.imshow('blackhat',blackhat)
cv2.imshow('closing',closing)
cv2.imshow('gradient',gradient)
cv2.imshow('opening',opening)
cv2.imshow('tophat',tophat)

cv2.waitKey(0)
cv2.destroyAllWindows()