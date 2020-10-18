
import numpy as np
import cv2

img = cv2.imread('/home/akshays/programs/learn.py/files.py/Artificial intelligence/opencv/resize/face.jpg',0)
rows,cols = img.shape

M = cv2.getRotationMatrix2D((cols/2,rows/2),45,3)
dst = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow('image',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

