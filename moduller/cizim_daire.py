import turtle

def ciz_daire():
    print("\n\nDaire çizimi")
    print("════════════")
    try:
        yaricap = int(input("Dairenin yarıçapını girin: "))
        if yaricap <= 0:
            print("Yarıçap pozitif bir sayı olmalıdır!")
            return

        turtle.circle(yaricap)
        print(f"Yarıçapı {yaricap} olan daire çizildi.")
        turtle.done()
    except ValueError:
        print("Geçersiz giriş! Lütfen bir sayı girin.")
    except Exception as e:
        print(f"Beklenmeyen hata: {e}")

if __name__ == "__main__":
    ciz_daire()
