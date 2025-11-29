import random

def adam_asmaca():
    words = ["python", "programlama", "bilgisayar", "oyun", "kod", "fonksiyon", "değişken"]
    word = random.choice(words).upper()
    guessed_letters = set()
    attempts = 6
    word_display = ["_" for _ in word]

    print("\n\nAdam Asmaca Oyunu")
    print("══════════════════")
    print("Kelimeyi tahmin edin! Harf girin veya kelimeyi tahmin edin.")
    print(f"Kalan hak: {attempts}")

    while attempts > 0 and "_" in word_display:
        print("\n" + " ".join(word_display))
        print(f"Tahmin ettiğiniz harfler: {' '.join(sorted(guessed_letters))}")

        try:
            guess = input("Tahmininiz: ").strip().upper()

            if not guess:
                print("Boş giriş! Lütfen bir harf veya kelime girin.")
                continue

            if len(guess) == 1:
                if guess in guessed_letters:
                    print("Bu harfi zaten tahmin ettiniz!")
                    continue

                guessed_letters.add(guess)

                if guess in word:
                    for i, letter in enumerate(word):
                        if letter == guess:
                            word_display[i] = guess
                    print("Doğru!")
                else:
                    attempts -= 1
                    print("Yanlış!")
            elif len(guess) == len(word):
                if guess == word:
                    word_display = list(word)
                    print("Tebrikler! Kelimeyi doğru tahmin ettiniz!")
                    break
                else:
                    attempts -= 1
                    print("Yanlış kelime!")
            else:
                print("Geçersiz giriş! Tek harf veya tam kelime girin.")
                continue

            print(f"Kalan hak: {attempts}")

        except KeyboardInterrupt:
            print("\nOyun sonlandırıldı.")
            break
        except Exception as e:
            print(f"Beklenmeyen hata: {e}")

    if "_" not in word_display:
        print(f"\nTebrikler! Kelime: {word}")
    else:
        print(f"\nKaybettiniz! Kelime: {word}")

if __name__ == "__main__":
    adam_asmaca()
