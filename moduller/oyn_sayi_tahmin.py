import random

def sayi_tahmin_oyunu():
    print("\n\nSayı Tahmin Oyunu")
    print("═══════════════════")

    try:
        max_sayi = int(input("Maksimum sayı nedir? (varsayılan 100): ") or 100)
        if max_sayi <= 0:
            print("Pozitif bir sayı girin!")
            return

        hedef_sayi = random.randint(1, max_sayi)
        tahmin_sayisi = 0

        print(f"1 ile {max_sayi} arası bir sayı tuttum. Tahmin et!")

        while True:
            try:
                tahmin = int(input("Tahmininiz: "))
                tahmin_sayisi += 1

                if tahmin < hedef_sayi:
                    print("Daha büyük bir sayı dene!")
                elif tahmin > hedef_sayi:
                    print("Daha küçük bir sayı dene!")
                else:
                    print(f"Tebrikler! {tahmin_sayisi} denemede bildiniz!")
                    break

            except ValueError:
                print("Geçersiz giriş! Lütfen bir sayı girin.")
            except KeyboardInterrupt:
                print("\nOyun sonlandırıldı.")
                break

    except ValueError:
        print("Geçersiz giriş! Lütfen pozitif bir sayı girin.")
    except Exception as e:
        print(f"Beklenmeyen hata: {e}")

if __name__ == "__main__":
    sayi_tahmin_oyunu()
