import os
folder = "mirror"
# alphabet = "abcdefghijklmnoprstuvyz"
files = os.listdir(folder)
sayac = 0
for i in files:
    sayac = "m" + sayac
    os.rename(os.path.join(folder,i),os.path.join(folder,str(sayac) + ".jpg"))
    sayac+=1
    print(os.path.join(folder,i))