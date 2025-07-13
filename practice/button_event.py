import tkinter as tk


def button_click(event):
    print("button clicked")


window = tk.Tk()


btn_click = tk.Button(master=window, text="click me")
btn_click.pack()

btn_click.bind("<Button-1>", button_click)

window.mainloop()
