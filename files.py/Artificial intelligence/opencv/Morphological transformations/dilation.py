import cv2
import numpy as np

img = cv2.imread('/home/akshays/programs/learn.py/files.py/Artificial intelligence/opencv/Morphological transformations/j.png')
kernel = np.ones((7,7))
dilation = cv2.dilate(img,kernel,iterations = 1)
cv2.imshow('image',img)
cv2.imshow('image1',dilation)
cv2.waitKey(0)
cv2.destroyAllWindows()

