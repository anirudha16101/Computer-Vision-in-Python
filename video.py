import numpy as np
import cv2

cap = cv2.VideoCapture('drop.avi')

while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame',gray)
    if cv2.waitKey(44) & 0xFF == ord('q'):
        break

cap.release(0)
cv2.destroyAllWindows()

