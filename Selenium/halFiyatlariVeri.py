from selenium import webdriver
from selenium.webdriver.common.by import By
import time


tarihler = []
aktarilacakTarih = []
urunler = []
birim = []
enDusuk = []
enYuksek = []
hepsi = []

driver = webdriver.Chrome()

url = "https://www.konya.bel.tr/hal-fiyatlari"

driver.get(url)
driver.maximize_window()
# time.sleep(2)


searchSelect = driver.find_element(By.ID, "tarih")

# time.sleep(1)
searchSelect.click()
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
    tableUrunler = driver.find_elements(By.CSS_SELECTOR, ".table tbody tr td")

    k = 0
    for j in tableUrunler:
        if k > 3:
            # aktarilacakTarih.append(i)
            hepsi.append(j.text)
        # if k == 0:
        #     urunler.append(j.text)
        # elif k == 1:
        #     birim.append(j.text)
        # elif k == 2:
        #     enDusuk.append(j.text)
        # else:
        #     enYuksek.append(j.text)
        k += 1
    # print(j.text)
    hepsi = [eleman for eleman in hepsi if eleman != ""]
    print("HEPSİ", hepsi)

    print("son eleman", hepsi[-1])

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
