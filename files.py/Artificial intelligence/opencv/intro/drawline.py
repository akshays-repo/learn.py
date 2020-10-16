import numpy as np
import cv2

# Create a black image
img = np.zeros((512,512,3))


# Draw a diagonal blue line with thickness of 5 px and starting and ending point
img = cv2.line(img,(0,0),(700,700),(255,0,0),5) 
cv2.imshow('image',img)
cv2.waitKey()
cv2.destroyAllWindows()
