print("╔═════════════════════╗")
print("║     HESAPLAMALAR    ║")
print("╠═════════════════════╣")
print("║  1-Hesap makinesi   ║")
print("║  2-Kare alan hesabi ║")
print("║  3-Kare çevre hesabi║")
print("║  4-Üçgen alan hesabi║")
print("║  5-Daire alan hesabi║")
print("║  6-                 ║")
print("║  7-                 ║")
print("║  8-Anamenu          ║")
print("║  9-Çıkış            ║")
print("║                     ║")
print("║    Seçimiz nedir?   ║")
print("╚═════════════════════╝")

while True:
    scm = input("Lütfen seçiminizi girin (1-5, 8 veya 9): ").strip()
    
    if scm == "1":
        print("Hesap makinesi seçildi.")
        num1 = int(input("İlk sayıyı girin: "))
        num2 = int(input("İkinci sayıyı girin: "))
        result = num1 + num2
        print("Toplam:", result)
    elif scm == "2":
        print("Kare alan hesabı yapılıyor.")
        import moduller.hsp_karea
    elif scm == "3":
        print("Kare çevre hesabı yapılıyor.")
        import moduller.hsp_karec
    elif scm == "4":
        print("Üçgen alan hesabı yapılıyor.")
        import moduller.hsp_ucgen
    elif scm == "5":
        print("Daire alan hesabı yapılıyor.")
        import moduller.hsp_daire
    elif scm == "8":
        print("ETKİN APP anamenüsüne dönülüyor...")
        break
    elif scm == "9":
        print("Hesaplamalar modülünden çıkış yapılıyor. Hoşça kalın!")
        exit()
    else:
        print("Geçersiz seçim. Lütfen 1-6, 8 veya 9'u seçin.")
