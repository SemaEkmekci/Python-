# Ad=Sema Nur EKMEKCİ
# No=21100011050


import random
import os

while True:
    alan=[]
    plan=[]
    def baslik():
        print("\t\t\t\t\t----------------------------------\n\t\t\t\t\t|\t\t\t\t |")
        print("\t\t\t\t\t|\tAmiral Battı Oyunu\t |\n\t\t\t\t\t----------------------------------")
    baslik()
    while True:
        boyut=int(input("""10 veya 10'dan büyük olacak şekilde;
        Oyun alanı boyutu giriniz-->"""))
        tut=boyut
        temp=boyut
        tut2=boyut
        if boyut<10:
            print("Hatali Giriş Yaptınız")
        else:
            break
    def oyunalani(boyut):
        print("\n")
        satirno=str(temp)
        i=boyut-1
        while boyut>0:
            alan.append([" ? "]*tut)
            boyut-=1
        while i>=0:
            j=0
            satir=""
            while j<tut2: 
                satir+=alan[i][j]
                j+=1
            satir=satirno+" "+satir
            print(f"\t\t\t\t\t  {satir}")
            print()
            i-=1
            satirno=str(int(satirno)-1)
            
    oyunalani(boyut)
    
    def gizlioyunalani(boyut):
        print("\n")
        satirno=str(temp)
        i=boyut-1
        while boyut>0:
            plan.append([" ? "]*tut)
            boyut-=1
        while i>=0:
            j=0
            satir=""
            while j<tut2: 
                satir+=plan[i][j]
                j+=1
            satir=satirno+" "+satir
            print(f"\t  {satir}")
            print()
            i-=1
            satirno=str(int(satirno)-1)

    def rastgele(temp):
        return random.randint(0,temp-1)
    while True:
        gemiler=[1,2,3,4]
        gemi_var=" 0 "
        secim=int(input("1)Gemileri siz mi yerleştirmek istersiniz?\n2)Gemiler rastgele mi yerleşsin?\n-->"))    
        if(secim==2):
            for i in gemiler:
                satir_numarasi=rastgele(temp)
                sutun_numarasi=rastgele(temp)
                yon=random.randint(0,1)
                if yon==0: 
                    konum=sutun_numarasi
                    kenar=temp-1
                    on=True
                    while(on):    
                            sutun_numarasi=rastgele(temp)
                            konum=sutun_numarasi
                            if i==2:
                                if sutun_numarasi==boyut-2 or sutun_numarasi==boyut-1: 
                                    sutun_numarasi=rastgele(temp)
                            elif i==3:
                                if sutun_numarasi==boyut-3 or sutun_numarasi==boyut-2 or sutun_numarasi==boyut-1: 
                                    sutun_numarasi=rastgele(temp)
                            elif i==4:
                                if sutun_numarasi==boyut-4 or sutun_numarasi==boyut-3 or sutun_numarasi==boyut-2 or sutun_numarasi==boyut-1: 
                                    sutun_numarasi=rastgele(temp)  
                            if konum+i<kenar:
                                on=False

                elif yon==1: 
                     konum = satir_numarasi
                     sutun=temp-1
                     on=True
                     while(on):
                        satir_numarasi=rastgele(temp)
                        konum = satir_numarasi
                        if i==2:
                            if sutun_numarasi==boyut-2 or sutun_numarasi==boyut-1: 
                                sutun_numarasi=rastgele(temp)
                        elif i==3:
                            if sutun_numarasi==boyut-3 or sutun_numarasi==boyut-2 or sutun_numarasi==boyut-1: 
                                    sutun_numarasi=rastgele(temp)
                        elif i==4:
                            if sutun_numarasi==boyut-4 or sutun_numarasi==boyut-3 or sutun_numarasi==boyut-2 or sutun_numarasi==boyut-1: 
                                sutun_numarasi=rastgele(temp)                           
                        if konum+i<sutun:
                            on=False
                    
                for a in range(i):
                    on=True
                    if yon==0:
                        while on:
                            gemi_var_mi=alan[satir_numarasi][sutun_numarasi+a]
                            if gemi_var_mi==gemi_var:
                                sutun_numarasi=rastgele(temp)
                            else:
                                on=False
                    else:
                        while on:
                            gemi_var_mi=alan[satir_numarasi+a][sutun_numarasi]
                            if gemi_var_mi==gemi_var:
                                sutun_numarasi=rastgele(temp)
                            else:
                                on=False

                if i==1:
                    gemi1satir=satir_numarasi
                    gemi1sutun=sutun_numarasi
                    gemi1yon=yon
                elif i==2:
                    gemi2satir=satir_numarasi
                    gemi2sutun=sutun_numarasi
                    gemi2yon=yon
                elif i==3:
                    gemi3satir=satir_numarasi
                    gemi3sutun=sutun_numarasi
                    gemi3yon=yon
                else:
                    gemi4satir=satir_numarasi
                    gemi4sutun=sutun_numarasi
                    gemi4yon=yon
                    


                for a in range(i):  
                    if yon==0:
                        alan[satir_numarasi][sutun_numarasi+a]=gemi_var
                    else:
                        alan[satir_numarasi+a][sutun_numarasi]=gemi_var            
            
            break
        elif(secim==1):
            yon_secim="1,0"
            for i in gemiler:
                istenilen_koordinatlar=input(f"(Satir numarasini aşağıdan yukarı doğru düşününüz!!!)\n{i} boyutlu geminiz için aralarında boşluk bırakarak sırasıyla\nsatır numarası, sütun numarasi, (0)yatay yada (1)dikey\ndeğerleri giriniz--> ")
                satir_numarasi,sutun_numarasi,yon = istenilen_koordinatlar.split(" ")
                satir_numarasi=int(satir_numarasi)
                sutun_numarasi=int(sutun_numarasi)
                if yon not in  yon_secim:
                    print("Hatalı Yön Girdiniz.")
                    break
                else:
                    yon=int(yon)
                    if yon==0: 
                        konum=sutun_numarasi-1
                        kenar=temp+1
                        if konum+i>kenar:
                            print("Gemi alana sığmıyor")
                            break
                    elif yon==1: 
                        konum = satir_numarasi
                        sutun=temp
                        if konum+i>temp:
                            print("Gemi alana sığmıyor")
                            break
                for a in range(i):    
                    if yon==0:
                        alan[satir_numarasi-1][sutun_numarasi-1+a]=gemi_var
                    else:
                        alan[satir_numarasi-1+a][sutun_numarasi-1]=gemi_var 
            break
        else:
            print("-->Hatalı Seçim")
    
    
    while True:
        mod=int(input("1)Gizli Mod\n2)Açık Mod-->\nMod Seçiniz-->"))
        if(mod==1):
            
            gizlioyunalani(boyut)
            break
        elif(mod==2):
            
            oyunalani(boyut)
            break
        else:
            print("Hatalı Seçim Yaptınız")
    
    atishakki=(temp**2)//3
    haktemp=atishakki
    yapilanatis=0
    sonkontrol=0
    batirilangemisayisi=0
    while(atishakki>0):
        kntrl=True
        ins=True
        while kntrl:
            while ins:
                atis=input("Atış yapmak istediğiniz koordinatları giriniz\n (aralarında bir boşluk bırakarak önce satır sonra sutun numarası)-->")
                satiratis,sutunatis=atis.split(" ")
                if int(satiratis)>temp or int(sutunatis)>temp:
                    print(">--Oyun alanının dşında değer girdiniz!!!--<")
                elif alan[int(satiratis)-1][int(sutunatis)-1]==' X ' or alan[int(satiratis)-1][int(sutunatis)-1]==" * ":
                 print("Daha önce bu konumu seçtiniz Lütfen başka bir konum seçiniz")
                elif alan[int(satiratis)-1][int(sutunatis)-1]==' X ' or alan[int(satiratis)-1][int(sutunatis)-1]==" * ":
                 print("Daha önce bu konumu seçtiniz Lütfen başka bir konum seçiniz")
                else:
                    ins=False
            sembol=alan[int(satiratis)-1][int(sutunatis)-1]
            if mod==2:

             if sembol==gemi_var:
                 alan[int(satiratis)-1][int(sutunatis)-1]=' X '
                 oyunalani(boyut)
                 print("Tebrikler bir gemi vurdunuz")
                 kntrl=False
             else:
                 alan[int(satiratis)-1][int(sutunatis)-1]=" * "
                 
                 
                 oyunalani(boyut)
                 print("Malesef isabet edemediniz")
                 kntrl=False
            else:
                # if alan[int(satiratis)-1][int(sutunatis)-1]==' X ' or alan[int(satiratis)-1][int(sutunatis)-1]==" * ":
                #  print("Daha önce bu konumu seçtiniz Lütfen başka bir konum seçiniz")
                if sembol==gemi_var:
                 alan[int(satiratis)-1][int(sutunatis)-1]=' X '
                 plan[int(satiratis)-1][int(sutunatis)-1]=' X '
                 
                 
                 gizlioyunalani(boyut)
                 print("Tebrikler bir gemi vurdunuz")
                 kntrl=False
                else:
                 alan[int(satiratis)-1][int(sutunatis)-1]=" * "
                 plan[int(satiratis)-1][int(sutunatis)-1]=' * '
                 
                 
                 gizlioyunalani(boyut)
                 print("Malesef isabet edemediniz")
                 kntrl=False
        yapilanatis+=1
        atishakki-=1
        puan=haktemp-yapilanatis
        print(f"Kalan atış hakkınız-->{puan}")
        
        if atishakki==0:
            if batirilangemisayisi!=3:
                print("Malesef Kaybettiniz")
                break
            else:
                print(f"TEBRİKLER TÜM GEMİLERİ BATIRDINIZ\nPuanınız-->{puan}")
                sonkontrol=1
                break
                
        elif(alan[gemi1satir][gemi1sutun]==" X "):
            print("Tebrikler 1 Boyutundaki gemiyi batırdınız")
            alan[gemi1satir][gemi1sutun]=" x "
            batirilangemisayisi+=1
        if gemi2yon==0:
            if(alan[gemi2satir][gemi2sutun]==" X " and alan[gemi2satir][gemi2sutun+1]==" X "):
                print("Tebrikler 2 Boyutundaki Gemiyi Batırdınız")
                alan[gemi2satir][gemi2sutun]=" x "
                alan[gemi2satir][gemi2sutun+1]=" x "
                batirilangemisayisi+=1
        if gemi3yon==0:
            if(alan[gemi3satir][gemi3sutun]==" X " and alan[gemi3satir][gemi3sutun+1]==" X " and alan[gemi3satir][gemi3sutun+2]==" X "):
                print("Tebrikler 3 Boyutundaki Gemiyi Batırdınız")
                alan[gemi3satir][gemi3sutun]=" x "
                alan[gemi3satir][gemi3sutun+1]=" x "
                alan[gemi3satir][gemi3sutun+2]=" x "
                batirilangemisayisi+=1            
        if gemi4yon==0:
            if(alan[gemi4satir][gemi4sutun]==" X " and alan[gemi4satir][gemi4sutun+1]==" X " and alan[gemi4satir][gemi4sutun+2]==" X " and alan[gemi4satir][gemi4sutun+3]==" X "):
                print("Tebrikler 4 Boyutundaki Gemiyi Batırdınız")
                alan[gemi4satir][gemi4sutun]=" x "
                alan[gemi4satir][gemi4sutun+1]=" x "
                alan[gemi4satir][gemi4sutun+2]=" x "
                alan[gemi4satir][gemi4sutun+3]=" x "
                batirilangemisayisi+=1
        if gemi2yon==1:
            if(alan[gemi2satir][gemi2sutun]==" X " and alan[gemi2satir+1][gemi2sutun]==" X "):
                print("Tebrikler 2 Boyutundaki Gemiyi Batırdınız")
                alan[gemi2satir][gemi2sutun]=" x "
                alan[gemi2satir+1][gemi2sutun]=" x "
                batirilangemisayisi+=1
        if gemi3yon==1:    
            if(alan[gemi3satir][gemi3sutun]==" X " and alan[gemi3satir+1][gemi3sutun]==" X " and alan[gemi3satir+2][gemi3sutun]==" X "):
                print("Tebrikler 3 Boyutundaki Gemiyi Batırdınız")
                alan[gemi3satir][gemi3sutun]=" x "
                alan[gemi3satir+1][gemi3sutun]=" x "
                alan[gemi3satir+2][gemi3sutun]=" x "
                batirilangemisayisi+=1            
        if gemi4yon==1:    
            if(alan[gemi4satir][gemi4sutun]==" X " and alan[gemi4satir+1][gemi4sutun]==" X " and alan[gemi4satir+2][gemi4sutun]==" X " and alan[gemi4satir+3][gemi4sutun]==" X "):
                print("Tebrikler 4 Boyutundaki Gemiyi Batırdınız")
                alan[gemi4satir][gemi4sutun]=" x "
                alan[gemi4satir+1][gemi4sutun]=" x "
                alan[gemi4satir+2][gemi4sutun]=" x "
                alan[gemi4satir+3][gemi4sutun]=" x "
                batirilangemisayisi+=1
        if batirilangemisayisi==4 and sonkontrol==0:
            print(f"TEBRİKLER TÜM GEMİLERİ BATIRDINIZ\nPuanınız-->{puan}")
            break

    giris_cikis=int(input("Tekrar Oynamak için 1'i \n Çıkmak için 0'ı tuşlayınız"))
    if giris_cikis==0:
        break
    elif giris_cikis==1:
        continue
    else:
        print("Hatali Seçim")
        continue