import sys
import tkinter as tk

win = tk.Tk()

def nothing():
    print("hello")

menubar=tk.Menu(win)
filemenu = tk.Menu(menubar)
filemenu.add_command(label='New Window',command=nothing)
filemenu.add_command(label='Open',command=nothing)
filemenu.add_separator()
filemenu.add_command(label='Exit',command=lambda:sys.exit(0))

editmenu=tk.Menu(menubar)
editmenu.add_command(label='Undo',command=nothing)
editmenu.add_command(label='Redo',command=nothing)
editmenu.add_separator()
editmenu.add_command(label='Cut',command=nothing)
editmenu.add_command(label='Copy',command=nothing)
editmenu.add_command(label='Paste',command=win.quit)


menubar.add_cascade(label="File",menu=filemenu)
menubar.add_cascade(label="Edit",menu=editmenu)


# menubar.pack()
win.config(menu=menubar)

win.mainloop()