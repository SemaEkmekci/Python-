from PIL import Image
import os


def yeniden_boyutlandir(klasor, hedef_klasor, genislik, yukseklik):
    # Hedef klasörü oluştur
    os.makedirs(hedef_klasor, exist_ok=True)

    # Dosyaları listele
    dosyalar = os.listdir(klasor)

    for dosya in dosyalar:
        # Dosya yolunu oluştur
        dosya_yolu = os.path.join(klasor, dosya)

        # Dosyanın bir resim dosyası olduğunu kontrol et
        if not os.path.isfile(dosya_yolu) or not dosya.lower().endswith(
            (".jpg", ".jpeg", ".png", ".gif")
        ):
            continue

        # Resmi aç
        resim = Image.open(dosya_yolu)

        # Boyutları değiştir
        yeniden_boyutlu_resim = resim.resize((genislik, yukseklik))

        # Yeni dosya yolunu oluştur
        yeni_dosya_yolu = os.path.join(hedef_klasor, dosya)

        # Yeni dosyayı kaydet
        yeniden_boyutlu_resim.save(yeni_dosya_yolu)


# Kullanım örneği
hedef_klasor = r"C:\Users\MUSTAFA\Desktop\gan_dataset\erozyon_resize"  # Yeni dosyaların kaydedileceği klasör
klasor = r"C:\Users\MUSTAFA\Desktop\gan_dataset\erozyon"  # İşlem yapılacak klasör
genislik = 1024
yukseklik = 640

yeniden_boyutlandir(klasor, hedef_klasor, genislik, yukseklik)
