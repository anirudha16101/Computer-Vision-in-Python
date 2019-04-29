import cv2
import numpy as np
 
cap= cv2.VideoCapture(1)


while (cap.isOpened()):
	ret,frame=cap.read() # -1, frame
	print("Returned: ", ret)
	cv2.imshow('frame',frame)
	if cv2.waitKey(1) & 0xFF== ord('q'):
		break
cap.release()
cv2.destroyAllWindows()
