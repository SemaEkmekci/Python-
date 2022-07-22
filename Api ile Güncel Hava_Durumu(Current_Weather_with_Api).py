import requests
import json

sehir_plaka = input("Şehir Plaka Bilgisi Giriniz-->")

city = {"adana":"01","adıyaman":"02","aksaray":"68","ardahan":"75",
"afyon":"03","ağrı":"04","amasya":"05","ankara":"06","antalya":"07",
"artvin":"08","aydın":"09","balıkesir":"10","bartın":"74","batman":"72",
"bayburt":"69","bilecik":"11","bingöl":"12","bitlis":"13","bolu":"14",
"burdur":"15","bursa":"16","çanakkale":"17","çankırı":"18","çorum":"19",
"denizli":"20","diyarbakır":"21","düzce":"81","edirne":"22","elazığ":"23",
"erzincan":"24","erzurum":"25","eskişehir":"26","gaziantep":"27","giresun":"28",
"gümüşhane":"29","hakkari":"30","hatay":"31","ığdır":"76","ısparta":"32",
"mersin":"33","istanbul":"34","izmir":"35","karabük":"78","karaman":"70",
"kars":"36","kastamonu":"37","kayseri":"38","kırıkkale":"71","kırklareli":"39",
"kırşehir":"40","kilis":"79","kocaeli":"41","konya":"42","kütahya":"43",
"malatya":"44","manisa":"45","kahramanmaraş":"46","mardin":"47","muğla":"48",
"muş":"49","nevşehir":"50","niğde":"51","ordu":"52","osmaniye":"80","rize":"53",
"sakarya":"54","samsun":"55","siirt":"56","sinop":"57","sivas":"58","şırnak":"73",
"tekirdağ":"59","tokat":"60","trabzon":"61","tunceli":"62","şanlıurfa":"63",
"uşak":"64","van":"65","yalova":"77","yozgat":"66","zonguldak":"67"}

# reversed_dict = dict(map(reversed, sehirler.items()))
sehirler={}
turkce_karakter={"ğ":"g","Ğ":"G","ç":"c","Ç":"C","ş":"s","Ş":"S","ü":"u","Ü":"U","ö":"o","Ö":"O","ı":"i","İ":"I"}

for key,value in city.items():
    sehirler[value] = key.capitalize()

for key,i in sehirler.items():
    indeks=0
    for j in i:
        if j in turkce_karakter:
            sehirler[key] = sehirler[key][0:indeks] + turkce_karakter[j] + sehirler[key][indeks+1:]  
        indeks+=1        

sehirler.get(sehir_plaka, "Yanlış Parametre")

sehir = sehirler[sehir_plaka]

            

url = "http://api.openweathermap.org/data/2.5/weather?q="+sehir+",tr&APPID=73bd7c41cb6165fd2182d68e5fb9dfd3"

response = requests.get(url)
json_format = json.loads(response.text)
sicaklik_degeri = int(json_format["main"]["temp"]-273)
print(str (sicaklik_degeri) +"°C")
result = json.loads(response.text)
