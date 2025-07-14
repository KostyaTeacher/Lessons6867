import tkinter as tk

# Створюємо головне вікно
root = tk.Tk()

# Створюємо фрейм для групування елементів
frame1 = tk.Frame(root, bg="blue")
frame1.pack(padx=10, pady=10)

# Додаємо лейбл у перший фрейм
label1 = tk.Label(frame1, text="Цей лейбл в першому фреймі")
label1.pack()

# Створюємо другий фрейм
frame2 = tk.Frame(root, bg="lightgreen")
frame2.pack(padx=10, pady=10)

# Додаємо кнопку у другий фрейм
button1 = tk.Button(frame2, text="Ця кнопка в другому фреймі")
button1.pack()

# Запускаємо головний цикл програми
root.mainloop()
