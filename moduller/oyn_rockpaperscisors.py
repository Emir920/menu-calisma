import random

def tas_kagit_makas():
    options = ["Taş", "Kağıt", "Makas"]
    english_options = ["Rock", "Paper", "Scissors"]
    option_map = dict(zip(english_options, options))

    user_score = 0
    computer_score = 0

    print("\n\nTaş Kağıt Makas Oyunu")
    print("══════════════════════")

    while True:
        try:
            user_choice = input("Taş, Kağıt veya Makas seçin (çıkmak için 'q' yazın): ").strip().capitalize()
            if user_choice.lower() == 'q':
                print(f"Oyun bitti! Siz: {user_score}, Bilgisayar: {computer_score}")
                break

            if user_choice not in options:
                print("Geçersiz seçim! Lütfen Taş, Kağıt veya Makas seçin.")
                continue

            computer_choice = random.choice(options)

            print(f"Siz seçtiniz: {user_choice}")
            print(f"Bilgisayar seçti: {computer_choice}")

            if user_choice == computer_choice:
                print("Berabere!")
            elif (user_choice == "Taş" and computer_choice == "Makas") or \
                 (user_choice == "Kağıt" and computer_choice == "Taş") or \
                 (user_choice == "Makas" and computer_choice == "Kağıt"):
                print("Kazandınız!")
                user_score += 1
            else:
                print("Bilgisayar kazandı!")
                computer_score += 1

            print(f"Skor: Siz {user_score} - Bilgisayar {computer_score}")
            print("-" * 30)

        except KeyboardInterrupt:
            print("\nOyun sonlandırıldı.")
            break
        except Exception as e:
            print(f"Beklenmeyen hata: {e}")

if __name__ == "__main__":
    tas_kagit_makas()
