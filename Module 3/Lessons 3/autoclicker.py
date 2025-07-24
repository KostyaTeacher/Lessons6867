import time
import tkinter as tk
from tkinter import messagebox
import keyboard
import mouse
import customtkinter as ctk

HEIGHT_SIZE = 640 // 2
WIDTH_SIZE = 600 // 2

running = False  # змінна, що зберігатиме стан: програма зараз працює або ні
delay = 0  # змінна, що зберігатиме тривалість перерви після кожного кліку

def start_clicker():
    global running, delay  # "знаходимо" змінні, що існують поза функцією
    clicks_per_second = int(entry.get())
    delay = 1 / clicks_per_second  # рахуємо затримку між кліками
    messagebox.showinfo("Auto Clicker", "Auto Clicker розпочинає роботу.")
    running = True
    # Запуск процесу кліків
    schedule_click()


def schedule_click():         # тут потім додамо клацання миші замість print

    while running:
        time.sleep(delay)  # затримка між кліками
        mouse.click()


def show_info(event):
    messagebox.showinfo("Інформація", "Це автоклікер, він буде клікати мишкою зі швидкістю, яку ти вкажеш!")

root = tk.Tk()
root.title("Auto Clicker")
root.geometry(f"{HEIGHT_SIZE}x{WIDTH_SIZE}")
root.configure(bg="#e0f7fa") # Light blue background

# Label: назва
title_label = tk.Label(root, text="Auto Clicker", font=("Trebuchet MS", 16, "bold"), bg="#e0f7fa", fg="#00796b")
title_label.pack(pady=10) # Add some padding

# Label: кліки на секунду
label = tk.Label(root, text="Кліків на секунду:", font=("Trebuchet MS", 12), bg="#e0f7fa", fg="#00796b")
label.pack(pady=5)

# Entry для кількості кліків
entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=5)

# Frame, в якому будуть кнопки "почати" і "вийти"
button_frame = tk.Frame(root, bg="#e0f7fa")
button_frame.pack(side=tk.BOTTOM, pady=(20, 30)) # Increase padding from the bottom
def exit_app():
    print("STOP")
    global running
    running = False
    messagebox.showinfo("Auto Clicker", "Auto Clicker зупинено.")
    root.destroy() # Закриття вікна Tkinter
# Кнопка "Почати"
start_button = tk.Button(button_frame, text="Почати", command=start_clicker, bg="#4caf50", fg="white", font=("Trebuchet MS", 12))
start_button.grid(row=0, column=0, padx=10) # Add horizontal padding

# Кнопка "Вийти"
exit_button = tk.Button(button_frame, text="Вийти", command=exit_app, bg="#f44336", fg="white", font=("Trebuchet MS", 12))
exit_button.grid(row=0, column=1, padx=10) # Add horizontal padding



keyboard.add_hotkey('esc', exit_app)


root.bind('i', show_info)
root.mainloop()