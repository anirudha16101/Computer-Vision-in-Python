import numpy as np
import matplotlib.pyplot as plt
import cv2


image= cv2.imread('water_balloons.jpg')
image_copy=np.copy(image)
image_copy= cv2.cvtColor(image_copy,cv2.COLOR_BGR2RGB)
plt.imshow(image_copy)


r=image_copy[:,:,0]
g=image_copy[:,:,1]
b=image_copy[:,:,2]

f,(ax1,ax2,ax3)=plt.subplots(1,3, figsize=(20,10))
print(f)
ax1.set_title('RED')
ax1.imshow(r,cmap='gray')


ax2.set_title('Green')
ax2.imshow(g,cmap='gray')

ax3.set_title('Blue')
ax3.imshow(b,cmap='gray')

lower_pink=np.array([180,0,100])
upper_pink= np.array([255,255,230])


mask_rgb= cv2.inRange(image_copy,lower_pink,upper_pink)
masked_image= np.copy(image_copy)

masked_image[mask_rgb==0]=[0,0,0]
plt.imshow(masked_image)
plt.show()

