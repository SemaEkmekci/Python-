import cv2
import numpy as np

vid = cv2.VideoCapture("traffic.avi")

while 1:
    _,frame = vid.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lower_yellow=np.array([18,94,150])
    upper_yellow=np.array([48,255,255])

    mask = cv2.inRange(hsv,lower_yellow,upper_yellow)
    cv2.imshow("Frame",frame)
    cv2.imshow("MASK",mask)

    if cv2.waitKey(20) & 0xFF==ord('q'):
        break

vid.release()
cv2.destroyAllWindows()

cv2.waitKey(0)
cv2.destroyAllWindows()