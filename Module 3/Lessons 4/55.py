import tkinter as tk

def hide_button():
    button1.pack_forget()

root = tk.Tk()
root.geometry("300x200")

button1 = tk.Button(root, text="Натисни, щоб зникнути", command=hide_button)
button1.pack()

root.mainloop()