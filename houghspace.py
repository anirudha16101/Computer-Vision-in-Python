import numpy as np
import matplotlib.pyplot as plt
import cv2

image=cv2.imread('phone.jpg')
image_copy= np.copy(image)

gray=cv2.cvtColor(image_copy,cv2.COLOR_BGR2GRAY)

low_threshold=50;
high_threshold=120;

edges=cv2.Canny(gray, low_threshold,high_threshold)
print edges

plt.imshow(edges,cmap='gray')
plt.show()

rho=1;
theta=np.pi/180
threshold=60 
max_line_length=110
max_line_gap=5;

lines=cv2.HoughLinesP(edges,rho,theta, threshold,np.array([]), max_line_length,max_line_gap)


lines_image=np.copy(image)
for line in lines:
	print line
	for x1,y1,x2,y2 in line:
		print x1
		cv2.line(lines_image,(x1,y1),(x2,y2),(255,0,0),5)
plt.imshow(lines_image)
plt.show()
