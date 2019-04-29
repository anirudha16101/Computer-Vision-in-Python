import numpy as np
import matplotlib.pyplot as plt
import cv2

image = cv2.imread('brain.jpg')
image_copy=np.copy(image)
image_copy= cv2.cvtColor(image_copy,cv2.COLOR_BGR2RGB)




gray= cv2.cvtColor(image_copy,cv2.COLOR_BGR2GRAY)
#CREATING A GAUSSIAN BLUR WITH FIELD AS STAN DARD DEVIATION AND SECOND FIELD IS KERNEL MATRIX ORDER

gray_blur =cv2.GaussianBlur(gray,(5,5),0)

f,(ax1,ax2)=plt.subplots(1,2, figsize=(20,10))

ax1.set_title('original_gray')
ax1.imshow(gray,cmap='gray')

ax2.set_title('blurred_image')
ax2.imshow(gray_blur,cmap='gray')
plt.show()

sobel_x= np.array([[-1, 0, 1],[-2,0,2 ],[-1,0,1]])


#convolution we use filter2d Function of cv

filtered= cv2.filter2D(gray,-1,sobel_x)
filtered_blured= cv2.filter2D(gray_blur,-1,sobel_x)


f,(ax1,ax2)=plt.subplots(1,2, figsize=(20,10))

ax1.set_title('original_gray')
ax1.imshow(filtered,cmap='gray')

ax2.set_title('blurred_image')
ax2.imshow(filtered_blured,cmap='gray')
plt.show()



