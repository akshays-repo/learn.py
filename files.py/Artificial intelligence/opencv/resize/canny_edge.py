import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('/home/akshays/programs/learn.py/files.py/Artificial intelligence/opencv/resize/face.jpg',0)

edges = cv2.Canny(img,300,200)#lower upper

plt.imshow(edges,cmap = 'copper')
plt.title('Edge Image')

plt.show()
