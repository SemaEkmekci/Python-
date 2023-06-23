from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

sayac = 0

tarihler = []
aktarilacakTarih = []
urunler = []
birim = []
enDusuk = []
enYuksek = []
veri = {}
tur = []

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
# /html/body/main/div[3]/div/div[1]/div[2]/div/table -> Sebze Fiyatları
# /html/body/main/div[3]/div/div[1]/div[3]/div/table -> Meyve Fiyatları
# /html/body/main/div[3]/div/div[1]/div[3]/div/table/tbody

print(type(tarihler[0]))
print("İLK TARİH---------------------------------------------------------------")
for i in tarihler:  # 1731
    print("-----------------------------------------------------------------------")
    gunAyYil = i.split(".")
    trh = gunAyYil[2] + "-" + gunAyYil[1] + "-" + gunAyYil[0]
    # i = i.replace(".", "-")

    url = "https://www.konya.bel.tr/hal-fiyatlari" + "?tarih=" + trh
    driver.get(url)
    time.sleep(2)
    # tableUrunler = driver.find_elements(By.CSS_SELECTOR, ".table tbody tr")
    tableSebze = driver.find_element(
        By.XPATH, "/html/body/main/div[3]/div/div[1]/div[2]/div/table/tbody"
    )
    tableMeyve = driver.find_element(
        By.XPATH, "/html/body/main/div[3]/div/div[1]/div[3]/div/table/tbody"
    )
    trSebze = tableSebze.find_elements(By.TAG_NAME, "tr")
    trMeyve = tableMeyve.find_elements(By.TAG_NAME, "tr")

    for j in trSebze[1:]:
        tds = j.find_elements(By.TAG_NAME, "td")
        k = 0
        for td in tds:
            if k == 0:
                urunler.append(td.text)
                tur.append("Sebze")
                aktarilacakTarih.append(i)
            elif k == 1:
                birim.append(td.text)
            elif k == 2:
                enDusuk.append(td.text)
            else:
                enYuksek.append(td.text)
            k += 1

        # print(j.text)
        urunler = [eleman for eleman in urunler if eleman != ""]
        # urunler = [eleman for eleman in urunler if eleman != "Ürün"]
        birim = [eleman for eleman in birim if eleman != ""]
        # birim = [eleman for eleman in birim if eleman != "Birim"]
        enDusuk = [eleman for eleman in enDusuk if eleman != ""]
        # enDusuk = [eleman for eleman in enDusuk if eleman != "En Düşük"]
        enYuksek = [eleman for eleman in enYuksek if eleman != ""]
        # enYuksek = [eleman for eleman in enYuksek if eleman != "En Yüksek"]

    for j in trMeyve[1:]:
        tds = j.find_elements(By.TAG_NAME, "td")
        k = 0
        for td in tds:
            if k == 0:
                urunler.append(td.text)
                tur.append("Meyve")
                aktarilacakTarih.append(i)
            elif k == 1:
                birim.append(td.text)
            elif k == 2:
                enDusuk.append(td.text)
            else:
                enYuksek.append(td.text)
            k += 1

        # print(j.text)
        urunler = [eleman for eleman in urunler if eleman != ""]
        # urunler = [eleman for eleman in urunler if eleman != "Ürün"]
        birim = [eleman for eleman in birim if eleman != ""]
        # birim = [eleman for eleman in birim if eleman != "Birim"]
        enDusuk = [eleman for eleman in enDusuk if eleman != ""]
        # enDusuk = [eleman for eleman in enDusuk if eleman != "En Düşük"]
        enYuksek = [eleman for eleman in enYuksek if eleman != ""]
        # enYuksek = [eleman for eleman in enYuksek if eleman != "En Yüksek"]

    # print("URUNLER", urunler)
    # print("BİRİM", birim)
    # print("ENDUŞÜK", enDusuk)
    # print("ENYÜKSEK", enYuksek)

    # print("Birim", birim)
    # print("EnDusuk", enDusuk)
    # print("EnYuksek", enYuksek)
    print("-----------------------------------------------------------------------")
    time.sleep(0.5)
    sayac += 1
    if sayac == 5:
        # for tarihBoyut in range(len(urunler)):

        print("Bittiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
        veri["Tarih"] = aktarilacakTarih
        veri["Ürün"] = urunler
        veri["Birim"] = birim
        veri["En Yüksek"] = enYuksek
        veri["En Düşük"] = enDusuk
        veri["Tür"] = tur
        df = pd.DataFrame(veri)
        df.to_excel("veriler2.xlsx", index=False)
        driver.quit()
        exit()

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
