import numpy as np
import cv2

# Create a black image
img = np.zeros((512,512,3))


img = cv2.ellipse(img,(256,256),(100,50),0,0,180,255,5) #center, axes, angle, startAngle, endAngle, color thickness
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
