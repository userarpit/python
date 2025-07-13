import tkinter as tk

# win = tk.Tk()
pw = tk.PanedWindow()
pw.pack(fill=tk.BOTH,expand=1)
left = tk.Entry(pw,bd=5)
pw.add(left)

pw2=tk.PanedWindow(pw,orient=tk.VERTICAL)
pw.add(pw2)

top=tk.Scale(pw2,orient=tk.HORIZONTAL)
pw2.add(top)


bottom=tk.Button(pw2,text="Click")
pw2.add(bottom)
tk.mainloop()