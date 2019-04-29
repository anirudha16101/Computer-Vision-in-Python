import numpy as np;
import matplotlib.pyplot as plt;
import cv2

image=cv2.imread('sunflower.jpg');
image_copy=np.copy(image)

image_copy=cv2.cvtColor(image_copy,cv2.COLOR_BGR2RGB)
plt.imshow(image_copy)
plt.show()


gray= cv2.cvtColor(image_copy,cv2.COLOR_BGR2GRAY)
plt.imshow(gray,cmap='gray')

plt.show()

# implementation of canny detector

lower= 120;
upper= 240;

edges=cv2.Canny(gray,lower,upper)
plt.imshow(edges,'gray')

plt.show()

wide=cv2.Canny(gray,20,100)
tight =cv2.Canny(gray,180,240)

f,(ax1,ax2)=plt.subplots(1,2,figsize=(10,20))

ax1.set_title('wide')
ax1.imshow(wide,cmap='gray')

ax2.set_title('tight')
ax2.imshow(tight, cmap='gray')


plt.show()
