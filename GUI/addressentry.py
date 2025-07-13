import tkinter as tk

window = tk.Tk()
window.title("Address Entry Form")
frame = tk.Frame(master=window,relief=tk.SUNKEN, borderwidth=3)
frame.pack()

lbl_first_name = tk.Label(master=frame,text="First Name :")
lbl_first_name.grid(row=0,column=0,sticky="e")

entry_first_name = tk.Entry(master=frame,width=50)
entry_first_name.grid(row=0,column=1,sticky="w")

lbl_last_name = tk.Label(master=frame,text="Last Name :")
lbl_last_name.grid(row=1,column=0,sticky="e")

entry_last_name = tk.Entry(master=frame,width=50)
entry_last_name.grid(row=1,column=1,sticky="w")

lbl_address_line_1 = tk.Label(master=frame,text="Address Line 1 :")
lbl_address_line_1.grid(row=2,column=0,sticky="e")

entry_address_line_1 = tk.Entry(master=frame,width=50)
entry_address_line_1.grid(row=2,column=1,sticky="w")

lbl_address_line_2 = tk.Label(master=frame,text="Address Line 2 :")
lbl_address_line_2.grid(row=3,column=0,sticky="e")

entry_address_line_2 = tk.Entry(master=frame,width=50)
entry_address_line_2.grid(row=3,column=1,sticky="w")

lbl_city = tk.Label(master=frame,text="City :")
lbl_city.grid(row=4,column=0,sticky="e")

entry_city = tk.Entry(master=frame,width=50)
entry_city.grid(row=4,column=1,sticky="w")

lbl_state_providence = tk.Label(master=frame,text="State/Providence :")
lbl_state_providence.grid(row=5,column=0,sticky="e")

entry_state_providence = tk.Entry(master=frame,width=50)
entry_state_providence.grid(row=5,column=1,sticky="w")

lbl_postal_code = tk.Label(master=frame,text="Postal Code :")
lbl_postal_code.grid(row=6,column=0,sticky="e")

entry_postal_code = tk.Entry(master=frame,width=50)
entry_postal_code.grid(row=6,column=1,sticky="w")

lbl_country = tk.Label(master=frame,text="Country :")
lbl_country.grid(row=7,column=0,sticky="e")

entry_country = tk.Entry(master=frame,width=50)
entry_country.grid(row=7,column=1,sticky="w")

frm_buttons = tk.Frame(master=window)
frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

btn_submit = tk.Button(master=frm_buttons, text="Submit")
btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)

btn_clear = tk.Button(master=frm_buttons, text="Clear")
btn_clear.pack(side=tk.RIGHT, ipadx=10)

window.mainloop()