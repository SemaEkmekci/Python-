import instaloader

profile_adi = input("İndirmek İstediginiz Profilin İsmini Giriniz: ")

print("Medya İndirilmeye Basliyor...")

instaloader.Instaloader().download_profile(profile_adi,profile_pic_only=False)

print("İndirme Tamamlandı")

