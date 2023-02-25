import cv2

cap = cv2.VideoCapture("blabla.mp4") # video dosyası okumak için
cap = cv2.VideoCapture(0) # webcam'den video okumak için

while True:
    ret, frame = cap.read() # 'read' fonksiyonu 2 deper döndürür. 'ret' değişkeni frame var olma veya olmama durumuna göre 'True' veya 'False değeri alır'. 'frame' ise videodaki kareleri alır.
    if ret == False:
        break
    frame = cv2.flip(frame,1)
    # flip fonksiyonu resmi ters çevirir. 2.parametre olarak 1 değeri verilirse y eksenine göre, 0 değeri verilirse x eksenine göre resmi dönderir.
    cv2.imshow("window",frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break    # Klavyeden 'q' hardine basıldığında pencere kapanır.
cap.release() # dosyayı kapatmak gibi bir işlevi vardır. Hata almamızı önler.
cv2.destroyAllWindows()