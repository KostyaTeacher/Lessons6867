import tkinter as tk

def change_to_green():
    root.configure(background='green')

def change_to_red():
    root.configure(background='red')

def change_to_blue():
    root.configure(background='blue')

root =tk.Tk()
root.title("Мій додаток")
root.geometry("300x300")
root.resizable(False, False)

menubar =tk.Menu(root)

color_menu =tk.Menu(menubar, tearoff=0)
color_menu.add_command(label="Зелений", command=change_to_green)
color_menu.add_command(label="Червоний", command=change_to_red)
color_menu.add_command(label="Синiй", command=change_to_blue)

menubar.add_cascade(label="Тема", menu=color_menu)

root.config(menu=menubar)

root.mainloop()