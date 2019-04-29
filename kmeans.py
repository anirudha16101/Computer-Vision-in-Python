import numpy as np
import matplotlib.pyplot as plt 
import cv2

image=cv2.imread('monarch.jpg')
image_copy=np.copy(image)
image_copy=cv2.cvtColor(image_copy,cv2.COLOR_BGR2RGB)
plt.imshow(image_copy)
plt.show()



#prepare data for k means
pixel_vals=image_copy.reshape((-1,3))
pixel_vals=np.float32(pixel_vals)

#implement the k Means clustring 
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.1)

## TODO: Select a value for k
# then perform k-means clustering
k = 2
retval, labels, centers = cv2.kmeans(pixel_vals, k, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

# convert data into 8-bit values
centers = np.uint8(centers)
segmented_data = centers[labels.flatten()]

# reshape data into the original image dimensions
segmented_image = segmented_data.reshape((image.shape))
labels_reshape = labels.reshape(image.shape[0], image.shape[1])

plt.imshow(segmented_image)

plt.show()

plt.imshow(labels_reshape==1,cmap='gray')
plt.show()


maskedimage=np.copy(image_copy)

maskedimage[labels_reshape==1]=[0,0,0]


plt.imshow(maskedimage)
plt.show()
