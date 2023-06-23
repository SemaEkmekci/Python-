import pandas as pd

# Sözlük yapısında veriler
veriler = {
    "tarih": ["01-01-2023", "02-01-2023", "03-01-2023"],
    "ürün": ["A", "B", "C"],
    "birim": [10, 15, 20],
    "endusuk": [5, 8, 7],
    "enyuksek": [15, 20, 25],
}

# Verileri pandas DataFrame'ine dönüştürme
df = pd.DataFrame(veriler)

# Excel tablosuna yazma
df.to_excel("veriler.xlsx", index=False)
