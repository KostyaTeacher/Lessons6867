import time
import customtkinter as ctk
from tkinter import messagebox
import keyboard
import mouse
import threading

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

running = False
delay = 0

HEIGHT_SIZE = 640 // 2
WIDTH_SIZE = 600 // 2

def start_clicker():
    global running, delay
    try:
        clicks_per_second = int(entry.get())
        if clicks_per_second <= 0:
            raise ValueError("Має бути більше нуля")
        delay = 1 / clicks_per_second
        messagebox.showinfo("Auto Clicker", "Auto Clicker розпочинає роботу.")
        running = True
        threading.Thread(target=schedule_click, daemon=True).start()
    except ValueError:
        messagebox.showerror("Помилка", "Введіть коректне число більше 0.")

def schedule_click():
    global running
    while running:
        time.sleep(delay)
        mouse.click()

def exit_app():
    global running
    running = False
    messagebox.showinfo("Auto Clicker", "Auto Clicker зупинено.")
    app.destroy()

def show_info(event=None):
    messagebox.showinfo("Інформація", "Це автоклікер, він буде клікати мишкою зі швидкістю, яку ти вкажеш!")

# Створення головного вікна
app = ctk.CTk()
app.title("Auto Clicker")
app.geometry(f"{HEIGHT_SIZE}x{WIDTH_SIZE}")

# Заголовок
title_label = ctk.CTkLabel(app, text="Auto Clicker", font=("Trebuchet MS", 20, "bold"))
title_label.pack(pady=15)

# Підпис до поля введення
label = ctk.CTkLabel(app, text="Кліків на секунду:", font=("Trebuchet MS", 14))
label.pack(pady=5)

# Поле введення
entry = ctk.CTkEntry(app, width=120, font=("Arial", 14))
entry.pack(pady=10)

# Кнопки
button_frame = ctk.CTkFrame(app)
button_frame.pack(pady=20)

start_button = ctk.CTkButton(button_frame, text="Почати", command=start_clicker, width=100)
start_button.grid(row=0, column=0, padx=10)

exit_button = ctk.CTkButton(button_frame, text="Вийти", command=exit_app, fg_color="red", hover_color="#cc0000", width=100)
exit_button.grid(row=0, column=1, padx=10)

# Гарячі клавіші
keyboard.add_hotkey('esc', exit_app)
app.bind('i', show_info)

# Запуск
app.mainloop()
