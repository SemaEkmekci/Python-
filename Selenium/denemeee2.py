from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

tarihler = []
aktarilacakTarih = []
urunler = []
birim = []
enDusuk = []
enYuksek = []
veri = {}

driver = webdriver.Chrome()

url = "https://www.konya.bel.tr/hal-fiyatlari"

driver.get(url)
driver.maximize_window()
# time.sleep(2)


searchSelect = driver.find_element(By.ID, "tarih")

# time.sleep(1)
# searchSelect.click()
# time.sleep(1)

result = driver.find_elements(By.CSS_SELECTOR, ".form-control option")


for element in result:
    tarihler.append(element.text)

tarihler.pop(0)

print(type(tarihler[0]))
print("İLK TARİH---------------------------------------------------------------")
for i in tarihler:
    print("-----------------------------------------------------------------------")
    gunAyYil = i.split(".")
    trh = gunAyYil[2] + "-" + gunAyYil[1] + "-" + gunAyYil[0]
    # i = i.replace(".", "-")

    url = "https://www.konya.bel.tr/hal-fiyatlari" + "?tarih=" + trh
    driver.get(url)
    time.sleep(5)
    tableUrunler = driver.find_elements(By.CSS_SELECTOR, ".table tbody tr")

    for j in tableUrunler:
        tds = j.find_elements(By.TAG_NAME, "td")
        k = 0
        for td in tds:
            if k == 0:
                urunler.append(td.text)
            elif k == 1:
                birim.append(td.text)
            elif k == 2:
                enDusuk.append(td.text)
            else:
                enYuksek.append(td.text)
            k += 1
        # print(j.text)
        urunler = [eleman for eleman in urunler if eleman != ""]
        urunler = [eleman for eleman in urunler if eleman != "Ürün"]
        birim = [eleman for eleman in birim if eleman != ""]
        birim = [eleman for eleman in birim if eleman != "Birim"]
        enDusuk = [eleman for eleman in enDusuk if eleman != ""]
        enDusuk = [eleman for eleman in enDusuk if eleman != "En Düşük"]
        enYuksek = [eleman for eleman in enYuksek if eleman != ""]
        enYuksek = [eleman for eleman in enYuksek if eleman != "En Yüksek"]
    for tarihBoyut in range(len(urunler)):
        aktarilacakTarih.append(i)
    print("Bittiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
    veri["Tarih"] = aktarilacakTarih
    veri["Ürün"] = urunler
    veri["Birim"] = birim
    veri["En Yüksek"] = enYuksek
    veri["En Düşük"] = enDusuk
    df = pd.DataFrame(veri)
    df.to_excel("veriler.xlsx", index=False)
    exit()
    # print("URUNLER", urunler)
    # print("BİRİM", birim)
    # print("ENDUŞÜK", enDusuk)
    # print("ENYÜKSEK", enYuksek)

    # print("Birim", birim)
    # print("EnDusuk", enDusuk)
    # print("EnYuksek", enYuksek)
    print("-----------------------------------------------------------------------")
    time.sleep(6)


# https://www.konya.bel.tr/hal-fiyatlari?tarih=2023-05-08
# https://www.konya.bel.tr/hal-fiyatlari?tarih=12-06-2023

# print(element.text)
# tableUrun = driver.find_elements(By.CSS_SELECTOR, ".form-control option")

# tableUrun = driver.find_elements(
#     By.XPATH, "/html/body/main/div[3]/div/div[1]/div[2]/div/table"
# )
# body > main > div:nth-child(3) > div > div.row > div:nth-child(2) > div > table > tbody


# driver.find_elements(
#     By.XPATH,
#     '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input',
# )


driver.close()
