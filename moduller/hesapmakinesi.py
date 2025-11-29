def display_menu():
    print("╔═════════════════════╗")
    print("║     HESAPLAMALAR    ║")
    print("╠═════════════════════╣")
    print("║  1-Hesap makinesi   ║")
    print("║  2-Kare alan hesabi ║")
    print("║  3-Kare çevre hesabi║")
    print("║  4-Üçgen alan hesabi║")
    print("║  5-Daire alan hesabi║")
    print("║  6-Dikdörtgen hesabi║")
    print("║  7-                 ║")
    print("║  8-Anamenu          ║")
    print("║  9-Çıkış            ║")
    print("║                     ║")
    print("║    Seçimiz nedir?   ║")
    print("╚═════════════════════╝")

def get_valid_choice():
    valid_choices = ["1", "2", "3", "4", "5", "6", "8", "9"]
    while True:
        try:
            scm = input("Lütfen seçiminizi girin (1-6, 8 veya 9): ").strip()
            if scm in valid_choices:
                return scm
            else:
                print("Geçersiz seçim. Lütfen 1-6, 8 veya 9'u seçin.")
        except KeyboardInterrupt:
            print("\nProgramdan çıkılıyor...")
            exit()
        except Exception as e:
            print(f"Beklenmeyen bir hata oluştu: {e}. Lütfen tekrar deneyin.")

def hesapmakinesi():
    actions = {
        "1": ("Hesap makinesi seçildi.", None),  # Placeholder for future calculator
        "2": ("Kare alan hesabı yapılıyor.", "moduller.hsp_karea"),
        "3": ("Kare çevre hesabı yapılıyor.", "moduller.hsp_karec"),
        "4": ("Üçgen alan hesabı yapılıyor.", "moduller.hsp_ucgen"),
        "5": ("Daire alan hesabı yapılıyor.", "moduller.hsp_daire"),
        "6": ("Dikdörtgen hesabı yapılıyor.", "moduller.hsp_dikdortgen"),
        "8": ("Anamenüye dönülüyor.", None),
        "9": ("Çıkış yapılıyor.", None)
    }

    while True:
        display_menu()
        scm = get_valid_choice()
        message, module = actions[scm]
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
            if scm == "8":
                print("ETKİN APP anamenüsüne dönülüyor...")
                break
            elif scm == "9":
                print("Hesaplamalar modülünden çıkış yapılıyor. Hoşça kalın!")
                exit()

if __name__ == "__main__":
    hesapmakinesi()
