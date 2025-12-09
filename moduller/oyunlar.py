def oyunlar():
    print("╔═════════════════════╗")
    print("║     OYUNLAR         ║") 
    print("╠═════════════════════╣")
    print("║  1-taş kağıt makas  ║")
    print("║  2- X O X           ║")
    print("║  3-sayı tahmini     ║")
    print("║  4-adam asmaca      ║")
    print("║  5-pokemon yazılı   ║")
    print("║  6-                 ║")
    print("║  7-                 ║")
    print("║  8-Anamenu          ║")
    print("║  9-Cikis            ║")
    print("║                     ║")
    print("║    Seçimiz nedir?   ║")
    print("╚═════════════════════╝")
    secim=input()
    if secim=="1":
        import moduller.oyn_rockpaperscisors
        moduller.oyn_rockpaperscisors.tas_kagit_makas()
    if secim=="2":
        import moduller.tıctactoe
        moduller.tıctactoe.board()
    if secim == "3":
        import moduller.oyn_sayi_tahmin
        moduller.oyn_sayi_tahmin.sayi_tahmin_oyunu()
    if secim == "4":
        import moduller.oyn_hangman
        moduller.oyn_hangman.adam_asmaca()
    if secim == "5":
        import moduller.oyn_pokemon
        moduller.oyn_pokemon.main()
    if secim=="9": exit()