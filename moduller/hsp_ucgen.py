print("\n\nÜçgen alan hesaplayici")
print("═══════════════════════")
try:
    taban = float(input("Üçgenin taban uzunlugu nedir? "))
    yukseklik = float(input("Üçgenin yüksekliği nedir? "))
    alan = (taban * yukseklik) / 2
    print(f"Üçgenin alanı {alan} birimdir.")
except ValueError:
    print("Geçersiz giriş! Lütfen sayı girin.")
