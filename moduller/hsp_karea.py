print("\n\nKare alan hesaplayici")
print("═══════════════════════")
try:
    kku = float(input("Kenar uzunlugu nedir? "))
    alan = kku * kku
    print(f"Karenin alani {alan} birimdir.")
except ValueError:
    print("Geçersiz giriş! Lütfen sayı girin.")
