def anamenu():
    print("╔═════════════════════╗")
    print("║     ETKİN APP       ║") 
    print("╠═════════════════════╣")
    print("║  1-Hesaplamalar     ║")
    print("║  2-Çizimler         ║")
    print("║  3-Oyunlar          ║")
    print("║  5-                 ║")
    print("║  6-                 ║")
    print("║  7-                 ║")
    print("║  8-                 ║")
    print("║  9-                 ║")
    print("║ 10-Cikiş            ║")
    print("║                     ║")
    print("║    Seçimiz nedir?   ║")
    print("╚═════════════════════╝") 
    secim = input()
    if secim =="1":
        print("Hesap yapmak istiyorsun demek.")
        import moduller.hesapmakinesi        

    if secim =="2":
        print("Çizim yapmak istiyorsun demek.")
        import moduller.cizimler

    if secim =="3": 
        import moduller.oyunlar

    if secim =="10" : exit()
anamenu()