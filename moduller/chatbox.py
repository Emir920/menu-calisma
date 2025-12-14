import tkinter as tk
from tkinter import scrolledtext
import datetime
import random
import ast
import operator

# Safe math operations
ops = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow
}

def safe_math(expr):
    def eval_node(node):
        if isinstance(node, ast.Num):
            return node.n
        if isinstance(node, ast.BinOp):
            return ops[type(node.op)](
                eval_node(node.left),
                eval_node(node.right)
            )
        raise ValueError("Invalid expression")
    return eval_node(ast.parse(expr, mode="eval").body)

def smart_reply(message):
    msg = message.lower()

    replies = {
        # English
        "hello": ["Hello!", "Hi there!", "Hey 👋"],
        "hi": ["Hi!", "Hello!"],
        "how are you": ["I'm doing great!", "All good 😄"],
        "your name": ["I'm a smart offline chatbot."],
        "help": ["Try asking math, time, date, or say hello."],
        "bye": ["Goodbye!", "See you later!"],
        # Turkish
        "merhaba": ["Merhaba!", "Selam!", "Merhaba, nasılsınız?"],
        "nasılsın": ["İyiyim, teşekkürler! 😊", "Harikayım! Siz nasılsınız?"],
        "adın ne": ["Ben bir akıllı chatbotum.", "Benim adım yok ama beni kullanabilirsiniz 🙂"],
        "yardım": ["Matematik sorabilir, saat veya tarih sorabilir, selamlaşabilirsiniz!"],
        "hoşça kal": ["Hoşça kal!", "Görüşürüz!"]
    }

    # Time & Date
    if "time" in msg or "saat" in msg:
        return datetime.datetime.now().strftime("Time: %H:%M:%S")
    if "date" in msg or "tarih" in msg:
        return datetime.datetime.now().strftime("Date: %Y-%m-%d")

    # Math
    try:
        if any(char.isdigit() for char in msg):
            return f"Answer: {safe_math(msg)}"
    except:
        pass

    # Pattern matching
    for key in replies:
        if key in msg:
            return random.choice(replies[key])

    return "Üzgünüm, bunu henüz anlamıyorum 🙂 / Sorry, I don't understand yet."

def send_message():
    message = user_input.get().strip()
    if not message:
        return

    chat_area.config(state=tk.NORMAL)
    chat_area.insert(tk.END, f"You: {message}\n")

    reply = smart_reply(message)
    chat_area.insert(tk.END, f"Bot: {reply}\n\n")

    chat_area.config(state=tk.DISABLED)
    user_input.delete(0, tk.END)
    chat_area.yview(tk.END)

# GUI setup
root = tk.Tk()
root.title("Bilingual Smart Chat Box")
root.geometry("450x550")

chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED)
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

input_frame = tk.Frame(root)
input_frame.pack(fill=tk.X, padx=10, pady=10)

user_input = tk.Entry(input_frame)
user_input.pack(side=tk.LEFT, fill=tk.X, expand=True)

send_button = tk.Button(input_frame, text="Send", command=send_message)
send_button.pack(side=tk.RIGHT)

root.bind("<Return>", lambda event: send_message())

root.mainloop()
