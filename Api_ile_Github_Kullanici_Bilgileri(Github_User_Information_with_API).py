from urllib import response
import pandas as pd
import requests
# import json
class Github:
    def __init__(self):
        self.api_url = "http://api.github.com"
        self.token = "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"
    def getuser(self, username):
        response = requests.get(self.api_url+'/users/'+username)
        return response.json()
    def getrepositories(self,username):
        response = requests.get(self.api_url+'/users/'+username+'/repos')
        return response.json()
    def createrepository(self,newrepositoryname):
        response = requests.post(self.api_url+'/user/repos?access_token='+ self.token , json ={
            "name" : newrepositoryname,
            "description" : "This is your first repository",
            "homepage" :"https://github.com",
            "private" : False,
            "has_issues" : True,
            "has_project" : True,
            "has_wiki" : True
        })
        return response.json()
github = Github()

while True:
    secim = input("\n1)Kullanıcı Arama\n2)Kullanıcının Repositorylerini Göster\n3)Repository Oluştur\n4)Çıkış\nSeçim--> ")
    
    if secim == '4':
        print("*"*5,"Çıkış Yapıldı","*"*5)
        break
    else:
        username = input("Kullanıcı Adı Giriniz-->")

        if secim == '1':
            user_json = github.getuser(username=username)
            user = {"informations":["Kullanıcı Adı" , "Oluşturma Tarihi" , "Son Güncelleme Tarihi" , "Repos Sayısı"] ,
            "data" : [user_json['name'],user_json['created_at'],user_json['updated_at'],user_json['public_repos']]
            }

            user_pd = pd.DataFrame(user)
            
            print("\n"*3,user_pd,"\n"*3)

        elif secim == '2':
            user_json = github.getrepositories(username=username)
            print("\n     Repositoryler     \n*************************\n")
            for i in range(len(user_json)):
                print(f"{i+1}){user_json[i]['name']}")
        elif secim == '3':
            newrepositoryname = input("Yeni Repository Adını Giriniz-->")
            print(github.createrepository(newrepositoryname=newrepositoryname))
        else:
            print("Yanlış Seçim")