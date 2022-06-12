# Sema Nur EKMEKCİ
# 21100011050

import datetime  # Programda tarih ve saat bilgisini sistemden almak için 
import time  # sleep methodunu kullanmaka için
arama=True # Arama fonksiyonunu hem silme hem arama fonksiyonunda kullandığım için arama mı silme mi yapmak istediğimizi ayırt etmek için
dk_ucreti=0.05 # Otopark dakika ücreti
otopark_alani=[]  # Otopark alanım 10*10 kare matris o yüzden 
yerler=set(" ") # dolu otopark alanlarını tutan bir küme. Kodda yer kontrolü yaparken kullanıyorum 
plakalar=set()  # Plakaları tutan bir küme. Kodda plaka kontrolü için kullanıyroum
def otopark(): # Otopark Alanımı oluşturuyor
    global yerler
    global otopark_alani
    otopark_alani=[]
    sira=0
    for i in range(0,10):
        satir=[" ? "]*10
        otopark_alani.append(satir) 
    try: 
        with open("21100011050(1).txt","r") as file:
            araba_yerleri=file.readlines()
        if "-" in araba_yerleri[0]:
            for i in araba_yerleri:
                liste=i.split("-")
                otopark_alani[int(liste[0])][int(liste[1])]=" X " 
        yerler=set(araba_yerleri)
    except IndexError:
        pass
    except FileNotFoundError: # Eğer dosyam yoksa kod çalışmayı bırakmadan yeni bir dosya açıyor
        with open("21100011050(1).txt","w",encoding="utf-8"):
            pass
    
    for i in range(0,10):
        col=""
        for j in range(0,10):
            col+=otopark_alani[i][j]
        print(f"\n{sira}) {col}")
        sira+=1


def zaman(): # Sistem tarih ve saatini alıyor
    now=datetime.datetime.now()
    return now

def AnaMenu(): # Sonsuz Döngüde AnaMenu() Fonksiyonum
    liste=["\n~~OTOPARK OTOMASYONU~~\n\n1)Otoparka Araba Ekle\n2)Otoparktan araba sil\n3)Otopark araba güncelle\n4)Otoparkta Araba Arama\n5)Otopark Araba Listesi \n6)Otopark Toplam Gelir Hesapla\n7)Otopark Dolu ve Boş Alanları Göster\n0)Çıkış"] # Daha Düzenli olması açısından printle yazmak yerine listede tuttum.
    for i in liste:
        print(i)
    secim=input("Seçiniz-->")
    if secim=="1":
        Ekle()
    elif secim=="2":
        Sil()
    elif secim=="3":
        Guncelleme()
    elif secim=="4":
        Arama()     
    elif secim=="5":
        Yazdir()
    elif secim=="6":
        Gelir_hesapla()
    elif secim=="7":
        Dolu_alan()
    elif secim=="0":
        exit()
    
def Ekle(): # Otoparka araba ekliyor
    plaka_dogru=True
    durum=1 # Otopark Alanının dolu olup olmamasına göre durum bilgim değişiyor
    global yerler
    global otopark_alani    
    try:    
        liste=Listeleme() # Dosyadaki bilgileri satır satır listeliyor
        for i in liste:
            i=i.split(",")
            plakalar.add(i[0]) # Plaka değerlerini kümeye kaydediyorum
    except (UnboundLocalError,TypeError):
        pass

    while durum:
        otopark() # Otopark Alanımı yazdırıyor
        araba_giris_saati=""
        araba_zamanı=zaman()
        araba_giris_saati=str(araba_zamanı.year)+" "+str(araba_zamanı.month)+" "+str    (araba_zamanı.day)+" "+str(araba_zamanı.hour)+" "+str(araba_zamanı.minute)
        araba_yeri=input("Araba yeri seçiniz(aralarında bir boşluk bırakarak önce satır sonra sütun)-->")
        satir_sutun=araba_yeri.split(" ")
        satir=int(satir_sutun[0]) # Otoparta arabayı ekleyeceğim satırı alıyorum
        sutun=int(satir_sutun[1]) # Otoparta arabayı ekleyeceğim sutunu alıyorum
        for i in yerler:
            if f"{satir}-{sutun}" in i: # Otopark alanının dolu olup olmadığını kontrol ediyor
                print("-->Otopark Alanı Dolu<--")
                durum=1 # Eğer otopark alanı dolu ise durum 1 olsun ki while döngüm devam etsin
                break
            else:
                durum=0
        if durum==0:          
            if "?" in otopark_alani[satir][sutun] :
                otopark_alani[satir][sutun]=" X  " # Otopark alanına "X" olarak arabayı ekliyor
            araba_plaka=input("Plaka-->")
            while plaka_dogru:
                if araba_plaka in plakalar:
                    print(f"--> {araba_plaka} plakalı araç otoparkta mevcut <--")
                    araba_plaka=input("Plaka-->")
                else:
                    plaka_dogru=False
            araba_sahibi=input("Araba Sahibi Adı ve Soyadı-->")
            telefon=input("Telefon-->")
            with open("21100011050(2).txt","a",encoding="utf-8") as file: # Dosyaya araba bilgilerini yazıyor
                file.write(f"{araba_plaka},{araba_giris_saati},{araba_sahibi},{telefon},{satir}-{sutun}\n")
            with open("21100011050(1).txt","a",encoding="utf-8") as file:
                file.write(f"{str(satir)}-{str(sutun)}\n")
            otopark()
    
    
def Sil():        
    with open("21100011050(1).txt","r",encoding="utf-8") as file:
        yer_listesi=file.readlines()    
    global arama
    arama=False
    Yazdir()
    liste=Listeleme()
    silinecek_veri=input("Silmek İstediğiniz arbanın plakasını giriniz-->")
    silinecek_veri_indis=Arama(silinecek_veri)
    arama=True
    def odeme(veri): # Otoparktan çıkış yapan arabanın ücretini hesaplıyor
        giden=""    
        sozluk=sozluk_yapisi() # Otoparktaki arabalarımın bilgilerini sözlüğe alıyor
        odenecek=sozluk[veri]["Giris_Zamanı"]
        giris=odenecek.split(" ")
        cikis=zaman()
        giden+=str(cikis.year)+" "+str(cikis.month)+" "+str(cikis.day)+" "+str(cikis.hour)  +" "+str(cikis.minute)
        cikis=giden.split(" ")
        zaman1=datetime.datetime(int(giris[0]),int(giris[1]),int(giris[2]),int(giris[3]),int    (giris[4]),0)  #Arabanın Giriş zamanını alıyor
        zaman2=datetime.datetime(int(cikis[0]),int(cikis[1]),int(cikis[2]),int(cikis[3]),int    (cikis[4]),0) # Arabanın çıkış zamanını alıyor
        fark=zaman2-zaman1
        dakika = divmod(fark.seconds, 60)
        tutar=(fark.days*1440+dakika[0])*dk_ucreti
        tutar=round(tutar,2)
        print(f"Toplam {fark.days*1140+dakika[0]} DAKİKA KALDI")
        print(f"Tutar--> {tutar} ₺")
        odeme_yapıldı_mı=input("Ödeme Yapıldı mı? [ 1-)EVET 2-)HAYIR ]-->")
        if odeme_yapıldı_mı=="1":
            with open("21100011050(3).txt","a",encoding="utf-8") as file:
                file.write(f"{silinecek_veri}-->{tutar}\n")   
        else:
            print("\n--->Ödeme Yapılmadığı İçin Araba Otoparktan Silinemiyor<---")
            return 0
    if silinecek_veri_indis!=None:
        deger=odeme(silinecek_veri)
        if deger!=0:
                print(f"\n=>Bilgilerine sahip araba  siliniyor... ")
                time.sleep(1)
                print("\n~~Silindi~~")
                liste.pop(silinecek_veri_indis)
                yer_listesi.pop(silinecek_veri_indis)
                with open("21100011050(2).txt","w",encoding="utf-8") as file:
                    for i in liste:
                        file.write(i)
                with open("21100011050(1).txt","w",encoding="utf-8") as file:
                    for i in yer_listesi:
                        file.write(i)


def Listeleme(): # Araba bilgilerimi listeye alıyor
    try:
        with open("21100011050(2).txt","r",encoding="utf-8") as file:
            liste=file.readlines()
        return liste
    except FileNotFoundError:
        with open("21100011050(2).txt","w",encoding="utf-8"):
            pass

def Yazdir(eleman="YOK"): # Arabaların bilgilerini ekrana yazdırıyor.
    arama_dogru=True
    dictionary=sozluk_yapisi()
    if eleman=="YOK": # Eğer arama veya silme yapılmıyorsa bu şartı kullanıyor
        otopark()
        for i in dictionary.keys():
            for j in dictionary[i].keys():
                if j == "Giris_Zamanı":
                    dictionary[i][j]=dictionary[i][j].split(" ")
                    tarih=dictionary[i][j][0]+"/"+dictionary[i][j][1]+"/"+dictionary[i][j][2]
                    saat=dictionary[i][j][3]+":"+dictionary[i][j][4]
                    dictionary[i][j]=tarih+" "+saat
                print(f"\n{j:13}: {dictionary[i][j]:13}")
                
            print("--------------------------")
    else: # Eğer arama veya silme yapılıyorsa bu şartı kullanıyor
        a=0
        for i in dictionary.keys():
            for j in dictionary[i].keys(): 
                yer=dictionary[i]["Araba_Yeri"].split("\n")
                dictionary[i]["Araba_Yeri"]=yer[0]
                if eleman == dictionary[i][j]:
                    yaz=i
                    a=1
                    for j in dictionary[yaz].keys(): 
                        if j == "Giris_Zamanı":
                            dictionary[i][j]=dictionary[i][j].split(" ")
                            tarih=dictionary[i][j][0]+"/"+dictionary[i][j][1]+"/"+dictionary[i][j][2]
                            saat=dictionary[i][j][3]+":"+dictionary[i][j][4]
                            dictionary[i][j]=tarih+" "+saat                         
                        print(f"\n{j:13}:{dictionary[yaz][j]:13}")
                   
        if a==0:
            arama_dogru=False
    return arama_dogru

def Arama (Kayit=""): # Arama yapıyor. Eğer silme yapmıyorsa kendi parametresini kullanıyor
    global arama
    kacıncı_eleman=None
    dogru=True
    durum=False

    liste=Listeleme()
    if arama==True:
        Yazdir()
        Kayit=input("Aradığınız Arabanın Herhangi Bir Bilgisini Tam olarak Giriniz-->")
    def kayit_var_mı():
        nonlocal kacıncı_eleman
        nonlocal durum
        nonlocal dogru
        for i in liste:
            if Kayit in i:
                kacıncı_eleman=liste.index(i)  
                dogru=Yazdir(Kayit)
                durum=True
                
    kayit_var_mı()
    if durum==False or dogru==False:
        print(f"{Kayit} bilgili araç yok")  
    return kacıncı_eleman   

def Guncelleme(): # Güncellemek istediğim arabanın istediğim bilgisini güncelliyor
    global arama
    arama=False
    liste=Listeleme()
    Yeni_Sozluk={}
    sozluk=sozluk_yapisi()
    Yazdir()
    guncellenecek_veri=input("Güncellemek istediğininz arabanın plakasını giriniz-->")
    silinecek_veri_indis=Arama(guncellenecek_veri)
    if silinecek_veri_indis!=None:
        print("1)Plaka\n2)Araba Sahibi\n3)Telefon\n4)Araba Yeri")
        secim=input("Güncellemek istediğiniz seçeneği işaretleyin-->")
        if secim=="1":
            guncel=input("Güncel Plaka-->")    
            for i in sozluk[guncellenecek_veri]:
                Yeni_Sozluk["Plaka"]=guncel+","
                Yeni_Sozluk["Giris_Zamanı"]=sozluk[guncellenecek_veri]["Giris_Zamanı"]+","
                Yeni_Sozluk["Araba_Sahibi"]=sozluk[guncellenecek_veri]["Araba_Sahibi"]+","
                Yeni_Sozluk["Telefon"]=sozluk[guncellenecek_veri]["Telefon"]+","
                Yeni_Sozluk["Araba_Yeri"]=sozluk[guncellenecek_veri]["Araba_Yeri"]
        if secim=="2":
            guncel=input("Güncel Araba Sahibi Adı ve Soyadı-->")    
            Yeni_Sozluk["Plaka"]=sozluk[guncellenecek_veri]["Plaka"]+","
            Yeni_Sozluk["Giris_Zamanı"]=sozluk[guncellenecek_veri]["Giris_Zamanı"]+","
            Yeni_Sozluk["Araba_Sahibi"]=guncel+","
            Yeni_Sozluk["Telefon"]=sozluk[guncellenecek_veri]["Telefon"]+","
            Yeni_Sozluk["Araba_Yeri"]=sozluk[guncellenecek_veri]["Araba_Yeri"]
        if secim=="3":
            guncel=input("Güncel Telefon-->")    
            Yeni_Sozluk["Plaka"]=sozluk[guncellenecek_veri]["Plaka"]+","
            Yeni_Sozluk["Giris_Zamanı"]=sozluk[guncellenecek_veri]["Giris_Zamanı"]+","
            Yeni_Sozluk["Araba_Sahibi"]=sozluk[guncellenecek_veri]["Araba_Sahibi"]+","
            Yeni_Sozluk["Telefon"]=guncel+","
            Yeni_Sozluk["Araba_Yeri"]=sozluk[guncellenecek_veri]["Araba_Yeri"]
        if secim=="4":
            otopark()
            guncel=input("Güncel Araba Yeri(Aralarında boşluk bırakarak önce satır sonra sütün  giriniz)-->")    
            Yeni_Sozluk["Plaka"]=sozluk[guncellenecek_veri]["Plaka"]+","
            Yeni_Sozluk["Giris_Zamanı"]=sozluk[guncellenecek_veri]["Giris_Zamanı"]+","
            Yeni_Sozluk["Araba_Sahibi"]=sozluk[guncellenecek_veri]["Araba_Sahibi"]+","
            Yeni_Sozluk["Telefon"]=sozluk[guncellenecek_veri]["Telefon"]+","
            guncel=guncel.split(" ")
            satir=guncel[0]
            sutun=guncel[1]
            guncel=satir+"-"+sutun
            Yeni_Sozluk["Araba_Yeri"]=guncel
            with open("21100011050(1).txt","a",encoding="utf-8") as file:
                file.write(f"{guncel}\n")
        liste.pop(silinecek_veri_indis) # Eski veriyi siliyor.
        with open("21100011050(2).txt","w",encoding="utf-8") as file:
            for i in liste:
                file.write(i)
            for i in Yeni_Sozluk.values():
                    file.write(i) # Güncellenen veriyi dosyaya yazdırıyor.
        guncel_araba_bilgileri=Listeleme()
        guncel_araba_yerleri=[]
        for i in guncel_araba_bilgileri:
            i=i.split(",")
            guncel_araba_yerleri+=[i[-1]]
        with open("21100011050(1).txt","w",encoding="utf-8") as file:
            for i in guncel_araba_yerleri:
                file.write(i)
    arama=True
    

def Gelir_hesapla(): # Otoparktan çıkış yapan bütün arabaların ödediği ücreti hesaplıyor ve otoparkın toplam gelirini hesaplıyor.
    toplam=0
    with open("21100011050(3).txt","r") as file:
        gelir_satiri=file.readlines()
    for i in range(len(gelir_satiri)):
        ucret=gelir_satiri[i].split(">")[1]
        toplam+=float(ucret)
    print(f"\n~~~ Toplam Gelir--> {toplam} ₺ ~~~")

def sozluk_yapisi(): # Otoparktaki bütün arabaların verilerini sözlüğe kaydediyor.
    liste=Listeleme()
    genel_sozluk={}
    for i in liste:
        sozluk_val=i.split(",")
        sozluk={}
        sozluk["Plaka"]=sozluk_val[0]
        sozluk["Giris_Zamanı"]=sozluk_val[1]
        sozluk["Araba_Sahibi"]=sozluk_val[2]
        sozluk["Telefon"]=sozluk_val[3]
        sozluk["Araba_Yeri"]=sozluk_val[4]
        genel_sozluk[sozluk_val[0]]=sozluk
    return genel_sozluk

def Dolu_alan(): 
    # Otoparktaki dolu alanları gösteriyor.
    doluyer=set()
    with open("21100011050(1).txt","r",encoding="utf-8") as yer:
        dolu=yer.readlines()
    if len(dolu)!=0:
        print("\n\nDolu Alanlar\n-------------------")    
        for i in dolu:
            doluyer.add(i)
            print(i)
        print("\n\nBoş Alanlar\n-------------------")    
        for i in range(0,10):
            for j in range(0,10):
                place=str(i)+"-"+str(j)
                if place not in doluyer:
                    print(place)
    else:
        print("~~Tüm alanlar boş~~") 
    
        
while True:
    AnaMenu()
