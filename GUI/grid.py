import tkinter as tk

window = tk.Tk()

for i in range(3):
    window.columnconfigure(i,weight=1,minsize=75)
    window.rowconfigure(i,weight=2,minsize=75)
    for j in range(3):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j, padx=5, pady=5)
        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.grid(row=i, column=j,padx=5, pady=5)
        # label.pack()

window.mainloop()