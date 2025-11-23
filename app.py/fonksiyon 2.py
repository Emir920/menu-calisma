def topla(a,b):
    return a+b


def carp(a,b):
    return a*b


def cikar(a,b):
    return a-b


def bol(a,b):
    return a/b


print(" HESAP MAKİNESİ")
print("  1-topla")
print("  2-çıkar")
print("  3-çarp")
print("  4-böl")


s = int(input ("Seçiminiz?"))
if not (s<1 or s>4):
    s1 = int(input("1.Sayıyı girin:"))
    s2 = int(input("2.Sayıyı girin:"))
    if s==1:
        print("Sonuç:",topla(s1,s2))
   
    if s==2:
        print("Sonuç:",cikar(s1,s2))
   
    if s==3:
        print("Sonuç:",carp(s1,s2))


    if s==4:
        print("Sonuç:",bol(s1,s2))
