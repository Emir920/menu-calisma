def carpim_tablosu():
    """
    Çarpım tablosunu gösterir.
    """
    for a in range(1, 11):
        print(f"\nBasamak: {a}")
        for b in range(1, 11):
            print(f"{a}x{b}={a*b}")
