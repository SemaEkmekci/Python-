from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# driver = webdriver.Chrome()

# url = "https://www.konya.bel.tr/hal-fiyatlari?tarih=2023-06-19"

# driver.get(url)

# time.sleep(2)
# driver.maximize_window()
# driver.save_screenshot("hal-fiyatlari.png")

# url = "https://www.konya.bel.tr/hal-fiyatlari?tarih=2023-06-15"

# driver.get(url)  # Sayfalar arası geçiş
# time.sleep(2)
# driver.back()

# print(driver.title)

# time.sleep(2)
# driver.close()

# Ders 4 Sayfa Etkileşimi

driver = webdriver.Chrome()

url = "https://www.konya.bel.tr/hal-fiyatlari?tarih=2023-06-19"

driver.get(url)

time.sleep(2)
driver.maximize_window()
# //*[@id="tarih"]

searchSelect = driver.find_element(By.ID, "tarih")

time.sleep(1)
searchSelect.click()
time.sleep(1)

result = driver.find_elements(By.CSS_SELECTOR, ".form-control option")

for element in result:
    print(element.text)


driver.close()
