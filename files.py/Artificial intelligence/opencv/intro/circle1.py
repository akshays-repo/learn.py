import numpy as np
import cv2

# Create a black image
img = np.zeros((512,512,3))

# Draw a diagonal red line with thickness of 5 px and starting and ending point
img = cv2.circle(img,(447,347), 100, (123,0,255), -1) #center radius color thickness
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
