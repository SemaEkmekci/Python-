import cv2

cv2.namedWindow("image",cv2.WINDOW_NORMAL) # 'cv2.namedWindow' yeni bir pencere oluşturur. 'cv2.WINDOW_NORMAL' pencereyi mouse ile boyutlandırmamızı sağlar.

img = cv2.imread("instagram_logo.png")

cv2.imshow("image",img)
cv2.imwrite("instagram.png",img) # resmi kaydetme
cv2.waitKey(0) # 1000 milisaniye 1 saniyeye eşdeğerdir. parametre olarak 0 değerini verirsek resim herhangi bir tuşa basılana kadar ekranda kalır.
cv2.destroyAllWindows() # Bütün pencereleri kapatır.