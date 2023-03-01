import cv2
import numpy as np

img = cv2.imread("veri.jpeg")
img = cv2.resize(img, (1920, 1080))
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

lower_blue=np.array([89,40,249],np.uint8)
upper_blue=np.array([114,80,105],np.uint8)

mask = cv2.inRange(hsv,lower_blue,upper_blue)
bitwise = cv2.bitwise_and(hsv, hsv, mask=mask)

cv2.imshow("Frame",img)
cv2.imshow("MASK",mask)
cv2.imshow("Bitwise",bitwise)

cv2.waitKey(0)
cv2.destroyAllWindows()