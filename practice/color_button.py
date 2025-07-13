import tkinter as tk
import random


def change_color():
    color_list = ["red", "orange", "yellow", "blue", "green", "indigo", "violet"]
    color = random.choice(color_list)
    btn_color['background'] = color


window = tk.Tk()

btn_color = tk.Button(
    master=window, text="Click me", command=change_color, fg="black"
)
btn_color.pack()
window.mainloop()
