sorular = [
    "Fransa'nın başkenti neresidir?",
    "İzmir'in plakası kaçtır?",
    "Tüplerde ne gazı bulunur?",
    "Zimbavye hangi kıtadadır?",
]
cevaplar = [
    "Paris",
    "35",
    "propan",
    "afrika",
]




sorulanlar =[]
devam ="Evet"
puan = 0
import random, math
while devam.lower() in ["evet","e","evt",""]:
    soruno = random.randint(0,len(sorular)-1)
    print("soruno:",soruno)
    if soruno not in sorulanlar:
        sorulanlar.append(soruno)
        cevap = input(sorular[soruno])
        if cevap.lower() == cevaplar[soruno].lower():
            puan += 100/len(sorular)
            print("bildin, puanın:", math.ceil(puan))
           
        else:
            print("bilemedin")
            puan -= 100/len(sorular)
            print("bildin, puanın:", math.ceil(puan))
       
        if len(sorulanlar)>=len(sorular): break
        else: devam=input("Devam etmek istiyor musun?\n(Devam için Evet yaz veya boş geç)")
else: print(f"Yarışmayı{puan}puanıyla tamamladın.")


