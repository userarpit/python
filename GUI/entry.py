import tkinter as tk
import time as t

window = tk.Tk()

def remove(name):
    name.delete(0)

def add(name):
    name.insert(0,'a')

name = tk.Entry()
name.pack()


button = tk.Button(text = "Remove",command=lambda:remove(name))
button.pack()

add_button = tk.Button(text = "Insert",command=lambda:add(name))
add_button.pack()
# t.sleep(60)
# window.destroy()
window.mainloop()