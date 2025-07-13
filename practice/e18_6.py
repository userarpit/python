import tkinter as tk

window = tk.Tk()

top_frame = tk.Frame(master=window, relief=tk.SUNKEN, borderwidth=5)
top_frame.pack(fill=tk.X)

lbl_first_name = tk.Label(master=top_frame, text="First Name:")
lbl_first_name.grid(row=0, column=0, sticky="e")

txt_first_name = tk.Entry(master=top_frame, width=30)
txt_first_name.grid(row=0, column=1)

lbl_last_name = tk.Label(master=top_frame, text="Last Name:")
lbl_last_name.grid(row=1, column=0, sticky="e")

txt_last_name = tk.Entry(master=top_frame, width=30)
txt_last_name.grid(row=1, column=1)

lbl_address_line_1 = tk.Label(master=top_frame, text="Address Line 1:")
lbl_address_line_1.grid(row=2, column=0, sticky="e")

txt_address_line_1 = tk.Entry(master=top_frame, width=30)
txt_address_line_1.grid(row=2, column=1)

lbl_address_line_2 = tk.Label(master=top_frame, text="Address Line 2:")
lbl_address_line_2.grid(row=3, column=0, sticky="e")

txt_address_line_2 = tk.Entry(master=top_frame, width=30)
txt_address_line_2.grid(row=3, column=1)

lbl_city = tk.Label(master=top_frame, text="City:")
lbl_city.grid(row=4, column=0, sticky="e")

txt_city = tk.Entry(master=top_frame, width=30)
txt_city.grid(row=4, column=1)

lbl_state_province = tk.Label(master=top_frame, text="State/Province:")
lbl_state_province.grid(row=5, column=0, sticky="e")

txt_state_province = tk.Entry(master=top_frame, width=30)
txt_state_province.grid(row=5, column=1)

lbl_postal_code = tk.Label(master=top_frame, text="Postal Code:")
lbl_postal_code.grid(row=6, column=0, sticky="e")

txt_postal_code = tk.Entry(master=top_frame, width=30)
txt_postal_code.grid(row=6, column=1)

lbl_country = tk.Label(master=top_frame, text="Country:")
lbl_country.grid(row=7, column=0, sticky="e")

txt_country = tk.Entry(master=top_frame, width=30)
txt_country.grid(row=7, column=1)

bottom_frame = tk.Frame(master=window)
bottom_frame.pack(fill=tk.X, side="right")

btn_clear = tk.Button(master=bottom_frame, text="Clear")
btn_clear.grid(row=0, column=0, padx=5, pady=5)

btn_submit = tk.Button(master=bottom_frame, text="Submit")
btn_submit.grid(row=0, column=1, padx=5, pady=5)

window.mainloop()
