import cv2
import numpy as np

img = cv2.imread('/home/akshays/programs/learn.py/files.py/Artificial intelligence/opencv/Morphological transformations/j.png')
kernel = np.ones((5,5),np.uint8)
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
cv2.imshow('image',img)
cv2.imshow('image1',tophat)
cv2.waitKey(0)
cv2.destroyAllWindows()


