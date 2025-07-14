import tkinter as tk

root = tk.Tk()

root.title("My super window")
root.geometry("900x1000")

label = tk.Label(root, text="⭐ Hello world!",
                 font=("Bahnschrift", 20),
                 fg = "green")

label2 = tk.Label(root, text="My first label",
                 font=("Times New Roman", 32),
                 fg="green",
                 bg="pink")

label3 = tk.Label(root, text = "<Дай відкуп або я тебе взламаю>",
                 font = ("Georgia", 32),
                 fg = "green",
                 bg = "black")

label4 = tk.Label(root, text="My first label",
                 font=("Times New Roman", 16), fg="green", bg="yellow")


label.pack()
label2.pack()
label3.pack()
label4.pack()

counter = 0

def info():
    global counter
    print(f"Кнопка натиснута {counter} разів")
    counter = counter + 1
    text = "⭐" + str(counter)
    label = tk.Label(root, text=text,
                     font=("Bahnschrift", 20),
                     fg="green")
    label.config(fg="turquoise")
    label.pack()

button = tk.Button(root, text="Натисни мене",
                   command=info)
button.pack()

def show_text():
    text = entry.get()
    print(text)

entry = tk.Entry(root)
entry.pack()

button2 = tk.Button(root, text="Показати текст",
                   command=show_text)
button2.pack()

root.mainloop()