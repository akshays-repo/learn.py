import numpy as np
import cv2

# Load an color image in grayscale
img = cv2.imread('/home/akshays/programs/learn.py/files.py/Artificial intelligence/opencv/intro/nature.jpg',1)
img2 = cv2.imread('/home/akshays/programs/learn.py/files.py/Artificial intelligence/opencv/intro/flower.jpg',0)

cv2.imshow('image1',img)
cv2.imshow('image2',img2)
cv2.waitKey()
cv2.destroyAllWindows()

