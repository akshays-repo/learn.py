import cv2
import numpy as np

img = cv2.imread('/home/akshays/programs/learn.py/files.py/Artificial intelligence/opencv/resize/face.jpg',0)
img1 = cv2.resize(img,(636,748))



cv2.imshow('img',img1)
cv2.imshow('imgorg',img)

cv2.waitKey(0)
cv2.destroyAllWindows()

