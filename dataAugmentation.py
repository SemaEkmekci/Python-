from PIL import Image,ImageOps
import os


files = os.listdir('original/')
formatlar=['jpg','png','tif']

for i in files:
    
    img = Image.open(os.path.join('original/', i))
    
    tut=i.split(".")[-1]
    ad=i.split(".")[0]
    if tut in formatlar:
        
        img_test = ImageOps.mirror(img)
        im_mirror = img_test.rotate(180)
        
        if tut=="jpg":
            filepath="mirror_rotate/{}.jpg".format(ad)
            im_mirror.save(filepath)
        
        elif tut=="png":
            filepath="mirror_rotate/{}.png".format(ad)
            im_mirror.save(filepath)
        
        else:
            filepath="mirror_rotate/{}.tif".format(ad)
            im_mirror.save(filepath)

# Mirror --> Sağı sola solu sağa yapıştırıyor. Yani aynadaki görüntümüz.
# Original rotate --> Saat yonu 180 derece.
# Mirror Rotate --> Aynadaki görüntünün saat yonunde 180 derece çevirilmiş hali.