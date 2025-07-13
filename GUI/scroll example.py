import tkinter as tk

win = tk.Tk()

s = tk.Scale(win)
s.pack()

sb = tk.Spinbox(win, from_ = 0, to_ = 10)
sb.pack()

scrollbar = tk.Scrollbar(win)
scrollbar.pack(side=tk.RIGHT,fill=tk.Y)

list = tk.Listbox(win, yscrollcommand=scrollbar.set)

for line in range(100):
    list.insert(tk.END,"line number " + str(line))

list.pack(side=tk.LEFT,fill=tk.BOTH)

win.mainloop()