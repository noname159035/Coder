import tkinter as tk, random, math
from tkinter import *
from PIL import ImageTk, Image

# вы находитесь на ветке MASTER


def coder():
    k = random.randint(2, 9)
    data = text.get("1.0", tk.END)
    text.delete("1.0", tk.END)
    out = ""
    for i in range(len(data)):
        out += str((ord(data[i]) * k) * math.factorial(k - 2)) + str(chr(random.randint(65, 90)))
    text.insert("1.0", out + str(k))


def decoder():
    data = text.get("1.0", tk.END)
    k = int(data[len(data) - 2])
    data = data[0:len(data) - 2]
    text.delete("1.0", tk.END)
    i_st = 0
    mas = []
    for i in range(len(data)):
        if not (data[i].isdigit()):
            mas.append(data[i_st: i])
            i_st = i + 1
    out = ""
    for i in range(len(mas)):
        out += chr(int((int(mas[i]) / math.factorial(k - 2)) / k))
    text.insert("0.0", out)

a = 1
print("привет")
window = tk.Tk()
window.title("CODER")
window.geometry('400x250')
window.resizable(width=False, height=False)
window['bg'] = "#3191BB"
text = Text(window, width=38, height=7)
text.place(x=45, y=30)
btn1 = Button(window, text="ЗАКОДИРОВАТЬ", command=coder, font=60)
btn1.place(x=10, y=160)
btn2 = Button(window, text="РАСКОДИРОВАТЬ", command=decoder, font=60)
btn2.place(x=200, y=160)
window.mainloop()
