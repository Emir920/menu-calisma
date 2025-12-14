def display_menu():
    """

    """
    print("╔═════════════════════╗")
    print("║     ETKİN APP       ║")
    print("╠═════════════════════╣")
    print("║  1-Hesaplamalar     ║")
    print("║  2-Çizimler         ║")
    print("║  3-Oyunlar          ║")
    print("║  4-python sınavı    ║")
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
    valid_choices = ["1", "2", "3", "4", "10"]
    while True:
        try:
            secim = input("Lütfen seçiminizi girin bu seçim hangisini açacağını belirler (1, 2, 3, 4 veya 10): ").strip()
            if secim in valid_choices:
                return secim
            else:
                print("Geçersiz seçim. Lütfen 1, 2, 3, veya 10'u seçin.")
        except KeyboardInterrupt:
            print("\nProgramdan çıkılıyor...")
            exit()
        except Exception as e:
            print(f"Beklenmeyen bir hata oluştu: {e}. Lütfen tekrar deneyin.")

def anamenu():
    """
    Main menu function for ETKİN APP.
    """
    while True:
        display_menu()
        secim = get_valid_choice()

        if secim == "1":
                import moduller.hesapmakinesi
                moduller.hesapmakinesi.hesapmakinesi()
        elif secim == "2":
                import moduller.cizimler
                moduller.cizimler.cizimler()
        elif secim == "3":
                import moduller.oyunlar
                moduller.oyunlar.oyunlar()
        elif secim == "4":
             import moduller.py_sınav
             moduller.py_sınav.run_quiz()
        elif secim == "10":
            print("ETKİN APP'den çıkış yapılıyor. Hoşça kalın!")

if __name__ == "__main__":
    anamenu()
