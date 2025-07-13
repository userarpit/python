import tkinter as tk
import random


def change_value():
    value = random.choice(list(range(1, 7)))
    lbl_value["text"] = value


window = tk.Tk()
window.rowconfigure([0, 1], weight=1, minsize=50)
window.columnconfigure(0, weight=1, minsize=50)

btn_roll = tk.Button(master=window, text="Roll", command=change_value)
btn_roll.grid(row=0, column=0, sticky="nsew")

lbl_value = tk.Label(master=window, text="")
lbl_value.grid(row=1, column=0, sticky="nsew")

window.mainloop()
