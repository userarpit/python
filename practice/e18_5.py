import tkinter as tk

window = tk.Tk()

btn_click_here = tk.Button(
    master=window, text="Click me", fg="blue", bg="white", width=50, height=25
)
btn_click_here.pack()

ent_name = tk.Entry(master=window, fg="black", bg="white", width=40)
ent_name.insert(0, "What is your name")
ent_name.pack()

window.mainloop()
