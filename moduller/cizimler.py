print("╔═════════════════════╗")
print("║     ÇİZİMLER        ║")
print("╠═════════════════════╣")
print("║  1-Kare çiz         ║")
print("║  2-Üçgen çiz        ║")
print("║  3-yıldız çiz       ║")
print("║  4-Daire çiz        ║")
print("║  5-Dikdörtgen çiz   ║")
print("║  6-panda çiz        ║")
print("║  7-pikachu ciz      ║")
print("║  8-Anamenu          ║")
print("║  9-Çıkış            ║")
print("║                     ║")
print("║    Seçimiz nedir?   ║")
print("╚═════════════════════╝")
secim=input()
if secim=="1":
    import moduller.cizim_kare
elif secim=="2":
    import moduller.cizim_ucgen
elif secim=="3":
    import moduller.cizim_yıldız
elif secim=="4":
    import moduller.cizim_daire
elif secim=="5":
    import moduller.cizim_dikdortgen
elif secim == "6":
    import moduller.panda_ciz
elif secim == "7":
    import moduller.pikachu_ciz
elif secim=="8":
    print("Anamenüye dönülüyor...")
elif secim=="9":
    print("Çizimler modülünden çıkış yapılıyor. Hoşça kalın!")
else: print("Geçersiz seçim.")
