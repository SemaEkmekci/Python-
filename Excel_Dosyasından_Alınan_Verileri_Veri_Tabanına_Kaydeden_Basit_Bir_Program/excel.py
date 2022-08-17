import pandas as pd
import mysql.connector
from baglanti import baglanti

veri = pd.read_excel('bılabılabıla')  # Adım-3
'''
# VERİ TABANINA  TABLO EKLEMEYE ÇALIŞTIM AMA SYNTAX HATASI ALIYORUM.

mycursor = baglanti.cursor()

basliklar = list(veri.columns)
sayac = 1
for i in basliklar:
    print(sayac,'->',i)
    sayac+=1
veri_tabaninda_olmali = input('Veri Tabanında olmasını istediğiniz başlıkların numarasını aralarında boşluk bırakarak giriniz-->Örn.(1 2 3)').split(' ')
veri_tabani_basliklari = list()

for i in veri_tabaninda_olmali:
    veri_tabani_basliklari.append(basliklar[int(i)-1])

tablo_olustur = f"('CREATE TABLE kurslar ({veri_tabani_basliklari[0]} VARCHAR(45), {veri_tabani_basliklari[1]} VARCHAR(45), {veri_tabani_basliklari[2]} VARCHAR(45))')"
mycursor.execute(tablo_olustur)

'''
kaydedilecek_veri_sayisi = int(input('Kaç Veri Kaydedilsin?'))

liste = veri.head(kaydedilecek_veri_sayisi)

veriler_tuple = list()

for i in range(len(liste)):
    veriler_tuple.append((veri.head(kaydedilecek_veri_sayisi)['title'][i],veri.head(kaydedilecek_veri_sayisi)['language'][i],veri.head(kaydedilecek_veri_sayisi)['url'][i]))  # Adım-4)





class veriler:
    baglanti = baglanti
    mycursor = baglanti.cursor()

    def __init__(self,title,language,url):
        self.baslik = title
        self.dil = language
        self.Url = url

    def saveData(SaveDate):
        sql = 'INSERT INTO kurslar (Başlık,Dil,Url) VALUES (%s,%s,%s)' # Adım-5)
        values = SaveDate
        veriler.mycursor.executemany(sql,values)
        try:
            veriler.baglanti.commit()
            print(f'{veriler.mycursor.rowcount} tane kayıt veritabanına eklendi.')
        except mysql.connector.Error as err:
            print('Hata->',err)
        finally:
            baglanti.close()
            print('Veritabanı bağlantısı kapatıldı.')

veriler.saveData(veriler_tuple)