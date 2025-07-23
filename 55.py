import tkinter as tk

fonts = [
    "Arial", "Arial Black", "Bahnschrift", "Calibri", "Cambria", "Cambria Math", "Candara",
    "Comic Sans MS", "Consolas", "Constantia", "Corbel", "Courier New", "Ebrima",
    "Franklin Gothic Medium", "Gabriola", "Gadugi", "Georgia", "Impact", "Ink Free",
    "Javanese Text", "Leelawadee UI", "Lucida Console", "Lucida Sans Unicode", "Malgun Gothic",
    "Microsoft Himalaya", "Microsoft JhengHei", "Microsoft New Tai Lue", "Microsoft PhagsPa",
    "Microsoft Sans Serif", "Microsoft Tai Le", "Microsoft YaHei", "Microsoft Yi Baiti",
    "Mongolian Baiti", "MS Gothic", "MV Boli", "Nirmala UI", "Palatino Linotype",
    "Segoe MDL2 Assets", "Segoe Print", "Segoe Script", "Segoe UI", "Segoe UI Historic",
    "Segoe UI Emoji", "Segoe UI Symbol", "SimSun", "Sitka Small", "Sylfaen", "Symbol",
    "Tahoma", "Times New Roman", "Trebuchet MS", "Verdana", "Webdings", "Wingdings",
    "Yu Gothic"
]

root = tk.Tk()
root.title("Всі системні шрифти Windows")
root.geometry("700x900")
root.configure(bg="white")

canvas = tk.Canvas(root, bg="white")
scroll_y = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
frame = tk.Frame(canvas, bg="white")

canvas.create_window((0, 0), window=frame, anchor='nw')
canvas.configure(yscrollcommand=scroll_y.set)

label_title = tk.Label(frame, text="🖋️ Максимально доступні шрифти Windows", font=("Arial", 20, "bold"), bg="white")
label_title.pack(pady=10)

for f in fonts:
    try:
        label = tk.Label(frame, text=f"Це шрифт: {f}", font=(f, 16), bg="white")
        label.pack(pady=5, anchor="w")
    except tk.TclError:
        label = tk.Label(frame, text=f"(Шрифт {f} не підтримується)", font=("Arial", 12, "italic"), fg="gray", bg="white")
        label.pack(pady=3, anchor="w")

frame.update_idletasks()
canvas.configure(scrollregion=canvas.bbox('all'))

canvas.pack(fill="both", expand=True, side="left")
scroll_y.pack(fill="y", side="right")

root.mainloop()