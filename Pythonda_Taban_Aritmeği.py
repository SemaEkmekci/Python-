while True:
    print("1)İkilik Tabandan Onluk Tabana Çevirme\n2)Onluk Tabandan İkilik Tabana Çevirme\n3)Çıkış")
    secim = int(input("  -->"))
    if secim==3:
        break
    elif secim == 1:
        bsayisi=0
        kntrl=0
        while True:
            num=input("Çevirmek İstediğiniz Sayıyı Giriniz\n -->")
            for x in num:
                kntrl=0
                bsayisi+=1
                result = 0  
                ikiliktaban="10"
            for a in num:  
                if a not in ikiliktaban:
                    print("Hatalı Giriş")
                    kntrl=-1
                    break
            for a in num:
                bsayisi-=1
                if int(a)==1:
                    sonuc = 2**(bsayisi)
                    result += sonuc
            if kntrl==0:
                print(result)   
                break         
    elif secim==2:
     num=int(input("Çevirmek İstediğiniz Sayıyı Giriniz\n -->"))
     sonuc=""
     while num>0:
         kalan=str(num%2)
         num=num//2
         sonuc += kalan
     print(sonuc[::-1])