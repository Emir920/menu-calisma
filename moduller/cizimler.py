def display_menu():
    print("╔═════════════════════╗")
    print("║     ÇİZİMLER        ║")
    print("╠═════════════════════╣")
    print("║  1-Kare çiz         ║")
    print("║  2-Üçgen çiz        ║")
    print("║  3-Daire çiz        ║")
    print("║  4-Yıldız çiz       ║")
    print("║  5-                 ║")
    print("║  6-                 ║")
    print("║  7-                 ║")
    print("║  8-Anamenu          ║")
    print("║  9-Çıkış            ║")
    print("║                     ║")
    print("║    Seçimiz nedir?   ║")
    print("╚═════════════════════╝")

def get_valid_choice():
    valid_choices = ["1", "2", "3", "4", "8", "9"]
    while True:
        try:
            secim = input("Lütfen seçiminizi girin (1-4, 8 veya 9): ").strip()
            if secim in valid_choices:
                return secim
            else:
                print("Geçersiz seçim. Lütfen 1-4, 8 veya 9'u seçin.")
        except KeyboardInterrupt:
            print("\nProgramdan çıkılıyor...")
            exit()
        except Exception as e:
            print(f"Beklenmeyen bir hata oluştu: {e}. Lütfen tekrar deneyin.")

def cizimler():
    actions = {
        "1": ("Kare çiziliyor.", "moduller.cizim_kare"),
        "2": ("Üçgen çiziliyor.", "moduller.cizim_ucgen"),
        "3": ("Daire çiziliyor.", "moduller.cizim_daire"),
        "4": ("Yıldız çiziliyor.", "moduller.cizim_yildiz"),
        "8": ("Anamenüye dönülüyor.", None),
        "9": ("Çizimler modülünden çıkış yapılıyor.", None)
    }

    while True:
        display_menu()
        secim = get_valid_choice()
        message, module = actions[secim]
        print(message)

        if module:
            try:
                __import__(module)
            except ImportError as e:
                print(f"Modül '{module}' yüklenirken hata oluştu: {e}")
                print("Lütfen modülün mevcut olduğundan emin olun.")
            except Exception as e:
                print(f"Modül yüklenirken beklenmeyen bir hata oluştu: {e}")
        else:
            if secim == "8":
                print("ETKİN APP anamenüsüne dönülüyor...")
                break
            elif secim == "9":
                print("Çizimler modülünden çıkış yapılıyor. Hoşça kalın!")
                exit()

if __name__ == "__main__":
    cizimler()
