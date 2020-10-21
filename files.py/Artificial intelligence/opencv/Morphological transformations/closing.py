import cv2
import numpy as np

img = cv2.imread('/home/akshays/programs/learn.py/files.py/Artificial intelligence/opencv/Morphological transformations/opening.jpg')
kernel = np.ones((5,5),np.uint8)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
cv2.imshow("image1",img)
cv2.imshow('image',closing)
cv2.waitKey(0)
cv2.destroyAllWindows()

