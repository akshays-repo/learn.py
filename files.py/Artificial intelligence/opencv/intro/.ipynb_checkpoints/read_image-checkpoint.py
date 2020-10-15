import numpy as np
import cv2

# Load an color image in grayscale
img = cv2.imread('nature.jpg')
img2 = cv2.imread('flower.jpg')

cv2.imshow('image',img)    #window name and image
cv2.imshow('image1',img2)
cv2.waitKey()
cv2.destroyAllWindows()
