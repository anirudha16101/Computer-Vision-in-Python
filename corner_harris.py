import numpy  as np
import matplotlib.pyplot as plt 
import cv2


image=cv2.imread('chess.png')
image_copy=np.copy(image)

image_copy=cv2.cvtColor(image_copy,cv2.COLOR_BGR2RGB)
plt.imshow(image_copy)
plt.show()


#detect corners
gray=cv2.cvtColor(image_copy,cv2.COLOR_BGR2GRAY)
gray=np.float32(gray)



dst=cv2.cornerHarris(gray,2,3,0.04)
dst=cv2.dilate(dst,None)
plt.imshow(dst,cmap='gray')
plt.show()


#Select and Display strong corners

thresh=0.01* dst.max()
corner_image=np.copy(image_copy)

for j in range(0,dst.shape[0]):
	for i in range(0, dst.shape[1]):
		if dst[j,i]>thresh:
			cv2.circle(corner_image,(i,j),2,(0,255,0),1)#image,centerpt,radius,color,thickness

plt.imshow(corner_image)
plt.show()




