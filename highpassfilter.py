import numpy as np 
import matplotlib.pyplot as plt
import cv2
image= cv2.imread('city_hall.jpg')
image_copy= np.copy(image)
image_copy= cv2.cvtColor(image_copy, cv2.COLOR_BGR2RGB)

plt.imshow(image_copy)
plt.show()


gray =cv2.cvtColor(image_copy, cv2.COLOR_BGR2GRAY)
plt.imshow(gray, cmap='gray')
plt.show()



#creating custom kernel for edge detection
# kernel == sobel_filter
sobel_x= np.array([[-1, 0, 1],[-2,0,2 ],[-1,0,1]])


#convolution we use filter2d Function of cv

filter_image= cv2.filter2D(gray,-1,sobel_x)
plt.imshow(filter_image,cmap='gray')
plt.show()

#creating binRY IMAGE
retval, binary_image= cv2.threshold(filter_image,50,255,cv2.THRESH_BINARY)
print(retval)
plt.imshow(binary_image,cmap='gray')
plt.show()
