import cv2
import numpy as np

img = cv2.imread('/home/akshays/programs/learn.py/files.py/Artificial intelligence/opencv/resize/face.jpg',0)
rows,cols = img.shape

M = np.float32([[1,0,100],[0,1,150]])
dst = cv2.warpAffine(img,M,(cols,rows)) #cv2.warpAffine takes a 2x3 transformation matrix

cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
