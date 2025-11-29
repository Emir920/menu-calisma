import math

print("\n\nDaire alan hesaplayici")
print("═══════════════════════")
try:
    yaricap = float(input("Dairenin yarıçapı nedir? "))
    alan = math.pi * yaricap ** 2
    print(f"Dairenin alanı {alan:.2f} birimdir.")
except ValueError:
    print("Geçersiz giriş! Lütfen sayı girin.")
