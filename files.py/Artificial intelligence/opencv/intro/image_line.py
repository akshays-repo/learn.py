import numpy as np
import cv2

img = cv2.imread('/home/akshays/programs/learn.py/files.py/Artificial intelligence/opencv/intro/nature.jpg',cv2.IMREAD_COLOR)
cv2.line(img,(0,0),(0,150),(0,255,255),15)
cv2.line(img,(0,150),(150,150),(0,255,255),15)
#start coordinates, end coordinates, color (bgr), line thickness.

cv2.rectangle(img,(15,25),(200,150),(0,0,255),15) #top left coordinate, bottom right coordinate, color, and line thickness.
cv2.circle(img,(100,63), 55, (0,255,0), -1)   #image, the center of the circle, the radius, color, and then thickness

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
