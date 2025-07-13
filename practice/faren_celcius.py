import tkinter as tk


def change():
    faren = ent_faren.get()
    celsius = (5 / 9) * (float(faren) - 32)
    lbl_celcius["text"] = f"{round(celsius,2)} \N{DEGREE CELSIUS}"


window = tk.Tk()
window.resizable(width=False, height=False)

frame = tk.Frame(master=window)
frame.pack()

ent_faren = tk.Entry(master=frame, width=10)
ent_faren.grid(row=0, column=0, sticky="e")

lbl_faren = tk.Label(master=frame, text="\N{DEGREE FAHRENHEIT}")
lbl_faren.grid(row=0, column=1, sticky="w")

btn_change = tk.Button(
    master=frame, text="\N{RIGHTWARDS BLACK ARROW}", command=change
)
btn_change.grid(row=0, column=2, sticky="nsew", padx=20, pady=20)

lbl_celcius = tk.Label(master=frame, text="0.0 \N{DEGREE CELSIUS}")
lbl_celcius.grid(row=0, column=4, sticky="w")

window.mainloop()
