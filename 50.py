import tkinter as tk

root = tk.Tk()

root.title("My super window")
root.geometry("500x500")
#root.resizable(False, False)

root.minsize(600, 600)            # не менше 600 px
root.maxsize(1000, 1000)           # не більше 1000 px

label = tk.Label(root, text="📳 Hello world!",
                 font=("Bahnschrift", 20),
                 fg = "#42FF6D", bg="#8D42FF",
                 padx = 600,) #pady=200)
label.pack()

root.mainloop()