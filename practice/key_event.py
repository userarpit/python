import tkinter as tk


def key_pressed(event):
    print(event.char)


window = tk.Tk()


window.bind("<Key>", key_pressed)

window.mainloop()
