# Ad:Sema Nur EKMEKCİ
# No:21100011050




boyut=int(input("5 veya 5'ten büyük bir boyut giriniz-->"))
karakter="*"
def sharfi(boyut):
    print("\n")
    ilksatir =""
    tut=boyut
    tut2=boyut
    tut3=boyut
    while boyut>0:
        ilksatir+=karakter
        boyut-=1
    print(ilksatir)
    tut2//=3
    while tut2>0:
        print(karakter)
        tut2-=1
    print(ilksatir)
    bosluk=""
    while tut-1>0:
        bosluk+=" "
        tut-=1
    bosluk+=karakter
    tut3//=3
    while tut3>0:
        print(bosluk)
        tut3-=1
    print(ilksatir)

def eharfi(boyut):
    print("\n")
    ilksatir=""
    tut=boyut
    tut2=boyut
    while boyut>0:
        ilksatir+=karakter
        boyut-=1
    print(ilksatir)
    tut//=3
    while tut>0:
        print(karakter)
        tut-=1
    print(ilksatir)
    tut2//=3
    while tut2>0:
        print(karakter)
        tut2-=1
    print(ilksatir)

def mharfi(boyut):
    print("\n")
    tut1=boyut//2-1
    satir=boyut-3
    tut2=boyut-2
    boyut//=2
    bosluk3=" "
    ilksatir=""
    ortasatir=""
    sonsatir=""
    bosluk=""
    while boyut>0:
        ilksatir+=karakter
        boyut-=1
    print(ilksatir*2+karakter)
    while tut1>0:
        bosluk+=" "
        tut1-=1
    ortasatir=karakter+bosluk+karakter+bosluk+karakter 
    while satir>0:
        print(ortasatir)
        satir-=1
    bosluk2=""
    while tut2>0:
        bosluk2+=" "
        tut2-=1
    sonsatir=karakter+bosluk2+karakter
    print(sonsatir)
    print(sonsatir)

def aharfi(boyut):
    tut=boyut
    kntrol=boyut//2
    sutun=boyut-1
    satir=boyut-2
    boyut-=2
    ortasatir=""
    ilksatir=""
    bosluk=" "
    bosluk2=""
    print("\n")
    ilksatir+=bosluk
    while boyut>0:
        ilksatir+=karakter
        boyut-=1
    print(ilksatir)
    bosluk2+=karakter
    while satir>0:
        bosluk2+=bosluk
        satir-=1
    bosluk2+=karakter
    while sutun>0:
        sutun-=1
        if sutun==kntrol:
            while tut>0:
                ortasatir+=karakter
                tut-=1
            print(ortasatir)
        else:
            print(bosluk2)
        
def charfi(boyut):
    print("\n")
    tut=boyut-2
    ilkvesonsatir=""
    while boyut>0:
        ilkvesonsatir+=karakter
        boyut-=1
    print(ilkvesonsatir)
    while tut>0:
        print(karakter)
        tut-=1
    print(ilkvesonsatir)

def iharfi(boyut):
    print("\n")
    bosluk=""
    bslk=boyut//2
    ilkvesonsatir=""
    tut=boyut-2
    while boyut>0:
        ilkvesonsatir+=karakter
        boyut-=1
    print(ilkvesonsatir)
    while bslk>0:
        bosluk+=" "
        bslk-=1
    ortacizgi=""
    ortacizgi+=bosluk+karakter
    while tut>0:
        print(ortacizgi)
        tut-=1
    print(ilkvesonsatir) 

def kharfi(boyut):
    print("\n")
    bslk=boyut-2
    temp=boyut-2
    str=boyut//2
    ortsttr=boyut//2+1
    ortasatir=""
    satir=""
    bosluk=""
    while str>0:
        while bslk>0:
            bosluk+=" "
            bslk-=1
        str-=1
        satir=karakter+bosluk+karakter
        print(satir)
        bslk=temp-1
        temp-=1
        bosluk=""
    while ortsttr>0:
        ortasatir+=karakter
        ortsttr-=1
    print(ortasatir)
    str=boyut//2
    bslk=boyut//2
    temp=boyut//2
    satir=""
    bosluk=""
    while str>0:
        while bslk>0:
            bosluk+=" "
            bslk-=1
        str-=1
        satir=karakter+bosluk+karakter
        print(satir)
        bslk=temp+1
        temp+=1
        bosluk=""


    

        



sharfi(boyut)
eharfi(boyut)
mharfi(boyut)
aharfi(boyut)
eharfi(boyut)
kharfi(boyut)
mharfi(boyut)
eharfi(boyut)
kharfi(boyut)
charfi(boyut)
iharfi(boyut)