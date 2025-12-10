
def run_quiz():
    questions = [
        {
            "question": "print(2 + 3) kodunun sonucu nedir?",
            "options": ["A) 5", "B) 23", "C) '23'", "D) Error"],
            "answer": "A"
        },
        {
            "question": "Aşağıdakilerden hangisi Python'da değiştirilebilir bir veri türüdür?",
            "options": ["A) Tuple", "B) String", "C) List", "D) Integer"],
            "answer": "C"
        },
        {
            "question": "Python'da bir fonksiyon tanımlamak için hangi anahtar kelime kullanılır?",
            "options": ["A) func", "B) def", "C) function", "D) define"],
            "answer": "B"
        },
        {
            "question": "Python'da for döngüsü nasıl başlatılır?",
            "options": ["A) for i in range(5):", "B) loop i from 1 to 5:", "C) for (i=0; i<5; i++):", "D) repeat 5 times:"],
            "answer": "A"
        },
        {
            "question": "Python'da tek bir satıra doğru şekilde yorum satırı eklemenin yolu nedir?",
            "options": ["A) // This is a comment", "B) /* This is a comment */", "C) # This is a comment", "D) <!-- This is a comment -->"],
            "answer": "C"
        }
    ]

    score = 0
    total_questions = len(questions)

    print("python testine hoş geldin!")
    print("her soruyu (A, B, C, veya D) yazarak cevapla.\n")

    for i, q in enumerate(questions, 1):
        print(f"Question {i}: {q['question']}")
        for option in q['options']:
            print(option)
        user_answer = input("Your answer: ").strip().upper()
        if user_answer == q['answer']:
            print("Doğru!\n")
            score += 1
        else:
            print(f"Yalnış cevap {q['answer']}.\n")

    print(f"Quiz completed! Your score: {score}/{total_questions}")
    percentage = (score / total_questions) * 100
    if percentage >= 80:
        print("Excellent! You have a strong understanding of Python basics.")
    elif percentage >= 60:
        print("Good job! Keep practicing to improve.")
    else:
        print("Keep learning! Review Python fundamentals and try again.")

if __name__ == "__main__":
    run_quiz()
