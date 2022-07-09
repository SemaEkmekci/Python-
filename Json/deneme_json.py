import json
import os
class User:
    def __init__(self,username, password, email):
        self.kullanici_adi = username
        self.sifre = password
        self.mail = email


class UserRepository:
    def __init__(self):
        self.users = []
        self.isloggedin = False
        self.currentUser = {}

        #load users from .json file
        self.loadusers()
    def loadusers(self):
        if os.path.exists('users.json'):
            with open('users.json','r',encoding='utf-8') as file:
                user = json.load(file)
                for i in user:
                    newuser = json.loads(i)
                    newUser = User(username=newuser['kullanici_adi'], password=newuser['sifre'], email=newuser['mail'])
                    self.users.append(newUser)
            # print(self.users)
    def register(self, user: User):
        self.users.append(user)
        self.savetoFile()
        print("Kullanıcı Oluşturuldu")
    
    def logout(self):
        if self.isloggedin:
            self.isloggedin = False
            print(f'Görüşürüzz {self.currentUser.kullanici_adi} ')
            self.currentUser = {}
        else:
            print("Giriş Yapmadınız")
    def kullanici_adi_goster(self):
        try:
            print(self.currentUser.kullanici_adi)
        except AttributeError:
            print("\n Giriş Yapılmadı ".center(40,'!'))
    def login(self, username, password):
        kontrol=0
        for i in self.users:
            if i.kullanici_adi == username and i.sifre == password:
                self.isloggedin = True
                self.currentUser = i
                print("Giriş Yapıldı".center(40,"~"))
                kontrol=1
                break
        if kontrol==0:
            print("Kayıt yok veya şifre veya email hatalı")
            
    def savetoFile(self):
        liste = []

        for user in self.users:
            liste.append(json.dumps(user.__dict__))
        with open("users.json","w") as file:
            json.dump(liste,file)

repository = UserRepository()

while True:
    print("Menü".center(50,"*"))
    secim = input(" 1-Kullanıcı oluştur \n 2-Giriş Yap \n 3-Oturumu Kapat \n 4-Kullanıcı Adı Göster \n 5-Kapat \n Seçiminiz-->")
    if secim=="5":
        break
    elif secim=="1":
        username = input("Username-->")
        password = input("Password-->")
        mail = input("E-mail-->")

        user = User(username=username,password=password,email=mail)

        repository.register(user)

    elif secim=="2":
        username = input("Username-->")
        password = input("Password-->")
        repository.login(username=username, password=password)
    elif secim=="3":
        repository.logout()
    elif secim=="4":
        repository.kullanici_adi_goster()
    else:
        print("Hatalı Seçim")    