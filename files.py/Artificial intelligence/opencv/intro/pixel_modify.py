import cv2
import numpy as np

img = cv2.imread('/home/akshays/programs/learn.py/files.py/Artificial intelligence/opencv/intro/flower.jpg')
img[100,100] = [255,255,255]
print (img[100,100])


cv2.imshow('image1',img)
cv2.waitKey()
cv2.destroyAllWindows()