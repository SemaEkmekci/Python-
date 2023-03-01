import cv2
import numpy as np



def nothing(x):
    pass


cv2.namedWindow("Tracbar")
cv2.resizeWindow("Tracbar", 500, 250)

cv2.createTrackbar("Lower-H", "Tracbar", 0, 180, nothing)
cv2.createTrackbar("Lower-S", "Tracbar", 0, 255, nothing)
cv2.createTrackbar("Lower-V", "Tracbar", 0, 255, nothing)

cv2.createTrackbar("Upper-H", "Tracbar", 0, 180, nothing)
cv2.createTrackbar("Upper-S", "Tracbar", 0, 255, nothing)
cv2.createTrackbar("Upper-V", "Tracbar", 0, 255, nothing)

cv2.setTrackbarPos("Upper-H", "Tracbar", 180)
cv2.setTrackbarPos("Upper-S", "Tracbar", 255)
cv2.setTrackbarPos("Upper-V", "Tracbar", 255)

frame = cv2.imread("veri.jpeg")
#frame = cv2.resize(frame, (1920, 1080))

while 1:
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lh = cv2.getTrackbarPos("Lower-H", "Tracbar")
    ls = cv2.getTrackbarPos("Lower-S", "Tracbar")
    lv = cv2.getTrackbarPos("Lower-V", "Tracbar")

    uh = cv2.getTrackbarPos("Upper-H", "Tracbar")
    us = cv2.getTrackbarPos("Upper-S", "Tracbar")
    uv = cv2.getTrackbarPos("Upper-V", "Tracbar")

    lower_color = np.array([lh, ls, lv])
    upper_color = np.array([uh, us, uv])

    mask = cv2.inRange(hsv, lower_color, upper_color)
    bitwise = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("original", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("bitwise", bitwise)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# vid.release()
cv2.destroyAllWindows()

cv2.waitKey(0)
cv2.destroyAllWindows()