import random
import tkinter as tk

window = tk.Tk()
window.columnconfigure(0, minsize=150)
window.rowconfigure([0, 1], minsize=50)

def roll():
    
    lbl_result["text"] = str(random.randint(1,6))    


btn_roll = tk.Button(window,text="Roll", command=roll)
lbl_result = tk.Label(window)

btn_roll.grid(row=0, column=0, sticky="nsew")
lbl_result.grid(row=1, column=0)


window.mainloop()