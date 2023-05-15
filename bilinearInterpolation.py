import cv2
import numpy as np
alphabet = "abcdefghijklmnoprstuvyz"

def resize_image_bilinear_interpolation(image, new_size):
    """
    image: NumPy array, ölçeklendirilecek resim
    new_size: Tuple, yeni boyut (genişlik, yükseklik)
    """
    # Yükseklik ve genişlik hesaplanır
    height, width = image.shape[:2]

    # Yeni boyutlar alınır
    new_width, new_height = new_size

    # Yükseklik ve genişlik oranları hesaplanır
    height_ratio = height / new_height
    width_ratio = width / new_width

    # Yeni boyutlara göre boş bir resim oluşturulur
    resized_image = np.zeros((new_height, new_width, 3), dtype=np.uint8)

    # Yeni boyutlardaki her bir piksel için orijinal resimdeki
    # piksellere karşılık gelen koordinatlar hesaplanır
    for y in range(new_height):
        for x in range(new_width):
            src_x = x * width_ratio
            src_y = y * height_ratio

            # Bilineer interpolasyon ile piksel değeri hesaplanır
            resized_image[y, x] = bilinear_interpolation(image, src_x, src_y)

    return resized_image


def bilinear_interpolation(image, x, y):
    """
    image: NumPy array, ölçeklendirilecek resim
    x: float, piksel x koordinatı
    y: float, piksel y koordinatı
    """
    # Orijinal resmin boyutu alınır
    height, width = image.shape[:2]

    # Koordinatlar tamsayı değilse, alttaki ve yanındaki pikseller seçilir
    x0 = int(x)
    x1 = min(x0 + 1, width - 1)
    y0 = int(y)
    y1 = min(y0 + 1, height - 1)

    # Oranlar hesaplanır
    tx = x - x0
    ty = y - y0

    # Her bir piksel için, 3 kanalın interpolasyonu yapılır
    pixel = np.zeros(3)
    for i in range(3):
        pixel[0] = (1 - tx) * image[y0, x0, i] + tx * image[y0, x1, i]
        pixel[1] = (1 - tx) * image[y1, x0, i] + tx * image[y1, x1, i]
        pixel[2] = (1 - ty) * pixel[0] + ty * pixel[1]

    return pixel.astype(np.uint8)


for i in range(20):
    dosyaYolu = "deneme\\"+str(i)+".jpg"
    img = cv2.imread(dosyaYolu)
    img2 = resize_image_bilinear_interpolation(img,(1024,640))

    imgName = str(i)+".jpg"
    # cv2.imshow("imageOriginal",img)
    # cv2.imshow("imageResized",img2)
    cv2.waitKey(0)
    cv2.imwrite(f"C:\\Users\\MUSTAFA\\Desktop\\kaydet\\{imgName}",img2)
    print("yazıldı")
