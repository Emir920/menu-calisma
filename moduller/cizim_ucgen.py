import turtle

def ciz_ucgen():
    print("\n\nÜçgen çizimi")
    print("════════════")
    try:
        kenar = int(input("Üçgenin kenar uzunluğunu girin: "))
        if kenar <= 0:
            print("Kenar uzunluğu pozitif bir sayı olmalıdır!")
            return

        for _ in range(3):
            turtle.forward(kenar)
            turtle.right(120)
        print(f"Kenar uzunluğu {kenar} olan üçgen çizildi.")
        turtle.done()
    except ValueError:
        print("Geçersiz giriş! Lütfen bir sayı girin.")
    except Exception as e:
        print(f"Beklenmeyen hata: {e}")

if __name__ == "__main__":
    ciz_ucgen()
