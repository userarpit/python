# from tkinter import *
import tkinter as tk
from tkinter import messagebox

win = tk.Tk()

# frame1 = Frame(win)
# frame1.pack()

# frame2 = Frame(win)
# frame2.pack(side=BOTTOM)

# rb = Button(frame1,text="Red",fg="red")
# rb.pack(side=LEFT)

# bb = Button(frame2,text="Blue",fg="blue")
# bb.pack(side=BOTTOM)

lb = tk.Listbox(win)
lb.insert(1,'python')
lb.insert(2,'c')
lb.insert(3,'c++')

lb.pack()

# top = tk.Toplevel()
# top.title("Second")
win.title("first")
def hello():
    messagebox.showinfo("hello","hi")
    return

b = tk.Button(win,text="popup",command=hello)
b.pack()

win.mainloop()