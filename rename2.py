from PIL import Image
import os


def yeniden_isimlendir(klasor, hedef_klasor):
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
        print(dosya[:-11])
        os.rename(
            os.path.join(klasor, dosya),
            os.path.join(hedef_klasor, str(dosya[:-11]) + ".jpg"),
        )


hedef_klasor = r"C:\Users\MUSTAFA\Desktop\gan_dataset\erozyon_rename"  # Yeni dosyaların kaydedileceği klasör
klasor = r"C:\Users\MUSTAFA\Desktop\gan_dataset\erozyon"  # İşlem yapılacak klasör


yeniden_isimlendir(klasor, hedef_klasor)

# folder = "normal_tme"
# # alphabet = "abcdefghijklmnoprstuvyz"
# files = os.listdir(folder)
# sayac = 0
# for i in files:
#     dosyaAd = "n" + str(sayac)
#     os.rename(os.path.join(folder, i), os.path.join(folder, str(dosyaAd) + ".jpg"))
#     sayac = int(sayac)
#     sayac += 1
#     print(os.path.join(folder, i))
