import cv2

cap = cv2.VideoCapture(0)
fileName = "webcam.avi" # videoyu kaydetmek istediğimiz dosyanın yolu
codec = cv2.VideoWriter_fourcc('W','M','V','2') # videoyu kaydetmek istediğimiz format hakkında bilgi
frameRate = 30
resolution = (640,480) # Çözünürlük değeri
videoFileOutput = cv2.VideoWriter(fileName, codec, frameRate, resolution)


while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)
    videoFileOutput.write(frame)
    cv2.imshow("Webcam",frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

videoFileOutput.release() # Serbest bırakma işlemi yapar.
cap.release() # Serbest bırakma işlemi yapar.
cv2.destroyAllWindows()