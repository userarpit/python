import tkinter as tk

window = tk.Tk()

border_effect = {
    "flat": tk.FLAT,
    "sunken": tk.SUNKEN,
    "raised": tk.RAISED,
    "groove": tk.GROOVE,
    "ridge": tk.RIDGE,
}

for relief_name,relief in border_effect.items():
    frame = tk.Frame(master=window,relief=relief,borderwidth=5)
    frame.pack(fill=tk.BOTH,expand=True)

    label = tk.Label(master=frame,text=relief_name)
    label.pack()

window.mainloop()