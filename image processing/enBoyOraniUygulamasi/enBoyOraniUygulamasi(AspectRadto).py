import cv2

def resizewithAspectRatio(img,width = None, height = None, inter = cv2.INTER_AREA):  # cv2.INTERAREA fonksiyonu hesaplamada herhangi bi hata olduğunda devreye girer. 
    
    dimension = None 
    (h,w) = img.shape[:2]
    
    if width is None and height is None: # Eğer herhangi bir boyut değeri girilmediyse resimde herhangi bir değişiklik yapılmadan geri döner.
        return img
    if width is None: # Eğer genişlik değeri girilmediyse aşağıdaki algoritmada yükseklik değeri kullanılarak genişlik değeri bulunur. 
        r = height / float(h)
        dimension = (int(w*r), height)
    else:
        r = height / float(w)
        dimension = (height,int(h*r))
        
    return cv2.resize(img, dimension, interpolation= inter)

img = cv2.imread("instagram_logo.png")

img2 = resizewithAspectRatio(img,None,300)
cv2.imshow("imageOriginal",img)
cv2.imshow("imageResized",img2)
cv2.waitKey(0)

