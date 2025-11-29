def display_menu():
    """
    Displays the main menu for ETKİN APP with ASCII art borders.
    """
    print("╔═════════════════════╗")
    print("║     ETKİN APP       ║")
    print("╠═════════════════════╣")
    print("║  1-Hesaplamalar     ║")
    print("║  2-Çizimler         ║")
    print("║  3-Oyunlar          ║")
    print("║  4-                 ║")
    print("║  5-                 ║")
    print("║  6-                 ║")
    print("║  7-                 ║")
    print("║  8-                 ║")
    print("║  9-                 ║")
    print("║ 10-Çıkış            ║")
    print("║                     ║")
    print("║    Seçimiz nedir?   ║")
    print("╚═════════════════════╝")

def get_valid_choice():
    """
    Prompts the user for a valid menu choice and returns it.
    Handles invalid inputs gracefully.
    """
    valid_choices = ["1", "2", "3", "10"]
    while True:
        try:
            secim = input("Lütfen seçiminizi girin (1, 2, 3 veya 10): ").strip()
            if secim in valid_choices:
                return secim
            else:
                print("Geçersiz seçim. Lütfen 1, 2, 3 veya 10'u seçin.")
        except KeyboardInterrupt:
            print("\nProgramdan çıkılıyor...")
            exit()
        except Exception as e:
            print(f"Beklenmeyen bir hata oluştu: {e}. Lütfen tekrar deneyin.")

def anamenu():
    """
    Main menu function that handles user selections and module imports.
    """
    actions = {
        "1": ("Hesap yapmak istiyorsun demek.", "moduller.hesapmakinesi"),
        "2": ("Çizim yapmak istiyorsun demek.", "moduller.cizimler"),
        "3": ("Oyun oynamak istiyorsun demek.", "moduller.oyunlar"),
        "10": ("Çıkış yapılıyor.", None)
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
            print("ETKİN APP'den çıkış yapılıyor. Hoşça kalın!")
            break

if __name__ == "__main__":
    anamenu()
