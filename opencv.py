import cv2
import numpy as np
import matplotlib.pyplot as plt 


img =cv2.imread('watch.jpg',cv2.IMREAD_GRAYSCALE)


print(img)
plt.imshow(img,cmap='gray',interpolation='bicubic') 
plt.show()
plt.waitKey(0)
plt.destroyAllWindows()
