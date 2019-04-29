import numpy as np
import cv2

cap = cv2.VideoCapture('drop.avi')

while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    lower_red=np.array([150,150,50])
    upper_red= np.array([180,255,150])
    mask=cv2.inRange(gray,lower_red,upper_red)
    res= cv2.bitwise_and(frame, frame,mask=mask)

    kernel= np.ones((15,15),np.float32 )/225
    smoothed= cv2.filter2D(res, -1,kernel )





    cv2.imshow('frame',gray)
    cv2.imshow('res', res)
    k= cv2.waitKey(5) & 0xFF
    if k==27:
        break;
	

cap.release(0)
cv2.destroyAllWindows()
