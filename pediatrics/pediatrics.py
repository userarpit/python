import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datetime
from dateutil.relativedelta import relativedelta
from PIL import Image, ImageTk
import database.pediatrics_database as dpd
import validate as v
import gc


def search_vd_in_given_data(vd, given_data):
    for gd in given_data:
        if gd[0] == vd[0] and gd[1] == vd[1]:
            return gd

    return None


def build_table(table_frame, vaccines_data, dob, given_data):
    headers = [
        "Age",
        "Vaccines",
        "Due On",
        "Given on",
        "Weight",
        "Height",
        "Drug name",
        "Batch No",
        "Mfg Date",
        "Expiry Date",
        "Comments",
    ]

    j = 0
    for header in headers:
        e = tk.Entry(
            table_frame,
            width=15,
            relief="solid",
            fg="white",
            bg="#008080",
            font=("Arial", 16, "bold"),
        )
        e.grid(row=0, column=j, padx=2, pady=3)
        e.insert(0, header)
        j += 1

    data = [[0] * 11 for i in range(27)]

    i = 1
    row_index = 0
    for vd in vaccines_data:
        for j in range(len(vd)):
            data[row_index][j] = tk.Label(
                table_frame, width=15, relief="solid", font=("Arial", 16)
            )
            data[row_index][j].grid(row=i, column=j, padx=2, pady=3)
            data[row_index][j].config(text=vd[j])

        j += 1

        data[row_index][j] = tk.Label(
            table_frame, width=15, relief="solid", font=("Arial", 16)
        )
        data[row_index][j].grid(row=i, column=j, padx=2, pady=3)

        match vd[0]:
            case "BIRTH":
                data[row_index][j].config(text=dob.strftime("%d-%m-%Y"))

            case "6 WEEKS":
                weeks_to_add = 6

                new_date = dob + datetime.timedelta(weeks=weeks_to_add)
                data[row_index][j].config(text=new_date.strftime("%d-%m-%Y"))

            case "10 WEEKS":
                weeks_to_add = 10

                new_date = dob + datetime.timedelta(weeks=weeks_to_add)
                data[row_index][j].config(text=new_date.strftime("%d-%m-%Y"))
            case "14 WEEKS":
                weeks_to_add = 14

                new_date = dob + datetime.timedelta(weeks=weeks_to_add)
                data[row_index][j].config(text=new_date.strftime("%d-%m-%Y"))
            case "6 MONTHS":
                months_to_add = 6

                new_date = dob + relativedelta(months=months_to_add)
                data[row_index][j].config(text=new_date.strftime("%d-%m-%Y"))

            case "9 MONTHS":
                months_to_add = 9

                new_date = dob + relativedelta(months=months_to_add)
                data[row_index][j].config(text=new_date.strftime("%d-%m-%Y"))

            case "12 MONTHS":
                months_to_add = 12

                new_date = dob + relativedelta(months=months_to_add)
                data[row_index][j].config(text=new_date.strftime("%d-%m-%Y"))

            case "15 MONTHS":
                months_to_add = 15

                new_date = dob + relativedelta(months=months_to_add)
                data[row_index][j].config(text=new_date.strftime("%d-%m-%Y"))
            case _:
                pass

        gd = search_vd_in_given_data(vd, given_data)

        for j in range(3, len(headers)):
            if gd and gd[j - 1] is not None:
                data[row_index][j] = tk.Label(
                    table_frame, width=15, relief="solid", font=("Arial", 16)
                )
                data[row_index][j].grid(row=i, column=j, padx=2, pady=3)
                data[row_index][j].config(text=gd[j - 1])
            else:
                data[row_index][j] = tk.Entry(
                    table_frame, width=15, relief="solid", font=("Arial", 16)
                )
                data[row_index][j].grid(row=i, column=j, padx=2, pady=3)
                data[row_index][j].insert(0, "")

        row_index += 1
        i += 1

    return data, headers


def add_scroll_bar(search_window):
    # Create a frame to hold the canvas and scrollbars
    frame = tk.Frame(search_window)
    frame.pack(fill="both", expand=True)

    # Create the canvas
    canvas = tk.Canvas(frame)
    canvas.grid(row=0, column=0, sticky="nsew")

    # Create the scrollbars
    x_scrollbar = tk.Scrollbar(frame, orient="horizontal", command=canvas.xview)
    x_scrollbar.grid(row=1, column=0, sticky="ew")
    y_scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
    y_scrollbar.grid(row=0, column=1, sticky="ns")

    # Configure the canvas to use the scrollbars
    canvas.configure(xscrollcommand=x_scrollbar.set, yscrollcommand=y_scrollbar.set)

    # Allow frame to expand with window resizing
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)

    # Create a frame inside the canvas for content
    inner_frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=inner_frame, anchor="nw")

    # Function to update scroll region when the size of the inner frame changes
    def update_scroll_region(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    inner_frame.bind("<Configure>", update_scroll_region)

    return inner_frame


def clear(
    first_name_obj,
    first_name_entry,
    last_name_entry,
    gender_radio_button,
    day_combo_box,
    month_combo_box,
    year_combo_box,
    Delivery_entry,
    Neonatal_Status_entry,
    Birth_Weight_entry,
    Length_entry,
    Head_circumference_entry,
    Chest_circumference_entry,
    blood_combo_box,
    Remarks_entry,
    Name_of_Mother_entry,
    mother_blood_combo_box,
    Name_of_Father_entry,
    father_blood_combo_box,
    Details_of_Siblings_entry,
    Phone_no_entry,
):
    first_name_obj.focus_set()
    first_name_entry.set("")
    last_name_entry.set("")
    gender_radio_button.set("")
    day_combo_box.set("")
    month_combo_box.set("")
    year_combo_box.set("")
    Delivery_entry.set("")
    Neonatal_Status_entry.set("")
    Birth_Weight_entry.set("")
    Length_entry.set("")
    Head_circumference_entry.set("")
    Chest_circumference_entry.set("")
    blood_combo_box.set("")
    Remarks_entry.set("")
    Name_of_Mother_entry.set("")
    mother_blood_combo_box.set("")
    Name_of_Father_entry.set("")
    father_blood_combo_box.set("")
    Details_of_Siblings_entry.set("")
    Phone_no_entry.set("")


def close(main_window):
    gc.collect()
    main_window.destroy()


def convert_dob(args):
    date = args.split()
    day = date[0]
    month = str(month_to_number(date[1]))
    year = date[2]

    full_date = month + "-" + day + "-" + year
    date_object = datetime.datetime.strptime(full_date, "%m-%d-%Y").date()
    return date_object


def full_gender(gender):
    match gender:
        case "M":
            return "Male"
        case "F":
            return "Female"


def search_screen(first_name_entry, last_name_entry, gender, dob):
    # declare search_window object
    search_window = tk.Tk()
    search_window.state("zoomed")
    search_window.title("Immunization Schedule")

    heading_frame = tk.Frame(search_window, border=10)
    heading_frame.pack()

    tk.Label(
        heading_frame, text="Immunization Schedule", fg="green", font=("Helvetica", 25)
    ).pack()

    tk.Label(
        search_window,
        text="Name: "
        + first_name_entry.capitalize()
        + " "
        + last_name_entry.capitalize(),
        fg="green",
        font=("Helvetica", 13),
    ).place(x=150, y=30)
    tk.Label(
        search_window,
        text="Gender: " + full_gender(gender),
        fg="green",
        font=("Helvetica", 13),
    ).place(x=400, y=30)
    tk.Label(
        search_window, text="DOB: " + dob, fg="green", font=("Helvetica", 13)
    ).place(x=1000, y=30)

    tk.Button(
        search_window,
        text="Back",
        width=10,
        font=("Helvetica", 10),
        fg="green",
        command=lambda: back(search_window),
    ).place(x=10, y=30)

    # add scrollbar to frame
    table_frame = add_scroll_bar(search_window)

    full_date = convert_dob(dob)
    # get the fixed part, and the vaccines given to the kid so far
    vaccines_data = dpd.get_vaccines_table()
    given_data = dpd.search(first_name_entry, last_name_entry, gender, full_date)

    data, headers = build_table(table_frame, vaccines_data, full_date, given_data)
    tk.Button(
        search_window,
        text="Edit",
        width=10,
        font=("Helvetica", 10),
        fg="green",
        command=lambda: edit(table_frame, data, headers),
    ).place(x=1270, y=30)
    tk.Button(
        search_window,
        text="Update",
        width=10,
        font=("Helvetica", 10),
        fg="green",
        command=lambda: update(
            first_name_entry, last_name_entry, gender, full_date, data, headers
        ),
    ).place(x=1395, y=30)
    search_window.bind("<Control-b>", lambda event: back(search_window))
    search_window.bind("<Control-e>", lambda event: edit(table_frame, data, headers))
    search_window.bind(
        "<Control-u>",
        lambda event: update(
            first_name_entry, last_name_entry, gender, full_date, data, headers
        ),
    )
    search_window.mainloop()


def search_window_function(main_window, *args):
    """
    args[0] -> first name of the child
    args[1] -> last name of the child
    args[2] -> gender
    args[3] -> dob
    """
    missing_list, missing = v.any_field_missing(
        "Search", args[0], args[1], args[2], args[3]
    )
    combined_missing_message = ""
    if missing:
        for missing_item in missing_list:
            combined_missing_message += missing_item
            combined_missing_message += "\n"

        messagebox.showinfo("Fields missing!", combined_missing_message)
    elif v.date_incorrect(args[3]):
        messagebox.showinfo("Incorrect DOB!", "Date of Birth not correct")
    elif dpd.baby_found(args[0], args[1], args[2], convert_dob(args[3])):
        main_window.destroy()
        search_screen(args[0], args[1], args[2], args[3])
    else:
        messagebox.showinfo("baby not found!", "baby not found")


def month_to_number(month_name):
    """Converts month name to month number."""
    month_dict = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12,
    }

    return month_dict.get(month_name)


def add_new_baby(main_window, *args):
    """
    args[0] -> first name of the child
    args[1] -> last name of the child
    args[2] -> gender
    args[3] -> date of birth
    args[4] -> delivery
    args[5] -> neonatal status
    args[6] -> birth weight
    args[7] -> length
    args[8] -> head circumference
    args[9] -> chest circumference
    args[10] -> blood group
    args[11] -> remarks
    args[12] -> Name of mother
    args[13] -> mother blood group
    args[14] -> name of father
    args[15] -> father blood group
    args[16] -> details of siblings
    args[17] -> phone number

    args[13] -> phone number
    """
    missing_list, missing = v.any_field_missing(
        "New",
        args[0],
        args[1],
        args[2],
        args[3],
        args[6],
        args[7],
        args[12],
        args[14],
        args[17],
    )
    combined_missing_message = ""
    if missing:
        for missing_item in missing_list:
            combined_missing_message += missing_item
            combined_missing_message += "\n"

        messagebox.showinfo("Fields missing!", combined_missing_message)
    elif v.phone_number_not_correct(args[17]):
        messagebox.showinfo("Phone number incorrect!", "Phone number is not correct!")
    else:
        full_date = convert_dob(args[3])
        dpd.add_new_baby_row(
            args[0],
            args[1],
            args[2],
            full_date,
            args[4],
            args[5],
            args[6],
            args[7],
            args[8],
            args[9],
            args[10],
            args[11],
            args[12],
            args[13],
            args[14],
            args[15],
            args[16],
            args[17],
        )
        messagebox.showinfo("Baby Added!", "baby added successfully!")


def edit(table_frame, data, headers):
    for row_index in range(dpd.get_number_of_row_vaccines()[0]):
        column_index = 3
        if type(data[row_index][column_index]) == tk.Label:
            for column_index in range(3, len(headers)):
                value = data[row_index][column_index].cget("text")

                data[row_index][column_index].destroy()

                data[row_index][column_index] = tk.Entry(
                    table_frame, width=15, relief="solid", font=("Arial", 16)
                )
                data[row_index][column_index].grid(
                    row=row_index + 1, column=column_index, padx=2, pady=3
                )
                data[row_index][column_index].insert(0, value)


def update(first_name, last_name, gender, dob, data, headers):
    final_data = []
    for row_index in range(dpd.get_number_of_row_vaccines()[0]):
        hold_data = []
        column_index = 3

        if type(data[row_index][column_index]) == tk.Entry:
            if data[row_index][column_index].get() != "":
                hold_data.append(row_index + 1)
                for column_index in range(3, len(headers)):
                    hold_data.append(data[row_index][column_index].get())
                final_data.append(hold_data)

    dpd.update_database(first_name, last_name, gender, dob, final_data)
    messagebox.showinfo("Record updated!", "Baby record updated succesfully")


def back(search_window):
    search_window.destroy()
    start_screen()


def create_label(main_window, labeltext, fontSize, x, y, fg):
    tk.Label(main_window, text=labeltext, font=("Helvetica", fontSize), fg=fg).place(
        x=x, y=y
    )


def create_entry(main_window, textvar, x, y, width):
    entry_obj = tk.Entry(main_window, textvariable=textvar, relief="solid", width=width)
    entry_obj.place(x=x, y=y)
    return entry_obj


def create_radio_button(main_window, x, y):
    gender_radio_button = tk.StringVar()
    options = ["M", "F"]
    for option in options:
        ttk.Radiobutton(
            main_window, text=option, variable=gender_radio_button, value=option
        ).place(x=x, y=y)
        x += 50
    return gender_radio_button


def create_combo_box(main_window, x, y, listvar, width):
    selected_option = tk.StringVar()
    ttk.Combobox(
        main_window,
        textvariable=selected_option,
        values=listvar,
        width=width,
        state="readonly",
    ).place(x=x, y=y)
    return selected_option


def main_screen(main_window):
    labeltextlist = [
        "Name of Child*",
        "Gender*",
        "Date of Birth*",
        "Delivery",
        "Neonatal Status",
        "Birth Weight*",
        "Length*",
        "Head circumference",
        "Chest circumference",
        "Blood Group",
        "Remarks",
        "Name of Mother*",
        "Mother's Blood Group",
        "Name of Father*",
        "Father of Blood Group",
        "Details of Siblings",
        "Phone no.*",
    ]

    labeltextselectedlist = ["Gender*", "Length*", "Chest circumference"]

    first_name_entry = tk.StringVar()
    last_name_entry = tk.StringVar()
    Neonatal_Status_entry = tk.StringVar()
    Birth_Weight_entry = tk.StringVar()
    Length_entry = tk.StringVar()
    Head_circumference_entry = tk.StringVar()
    Chest_circumference_entry = tk.StringVar()
    Remarks_entry = tk.StringVar()
    Name_of_Mother_entry = tk.StringVar()
    Name_of_Father_entry = tk.StringVar()
    Details_of_Siblings_entry = tk.StringVar()
    Phone_no_entry = tk.StringVar()
    Delivery_entry = tk.StringVar()

    today = datetime.date.today()
    year = today.year

    days = list(range(1, 32))
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    years = list(range(2013, year + 1))

    blood_group_list = ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]

    # declare Frame
    main_frame = tk.Frame(main_window, width=750, height=750, border=10)
    main_frame.place(x=700, y=20)

    # create top Label
    create_label(main_frame, "Immunization\n    & Health Record\n", 25, 0, 0, "#A020F0")

    x = 30
    y = 90
    for labeltext in labeltextlist:
        if labeltext in labeltextselectedlist:
            match labeltext:
                case "Gender*":
                    create_label(main_frame, labeltext, 15, x + 540, y, "#343434")
                    gender_radio_button = create_radio_button(main_frame, x + 630, y)

                case "Length*":
                    create_label(main_frame, labeltext, 15, x + 450, y, "#343434")
                    create_entry(main_frame, Length_entry, x + 530, y, 28)

                case "Chest circumference":
                    create_label(main_frame, labeltext, 15, x + 380, y, "#343434")
                    create_entry(main_frame, Chest_circumference_entry, x + 580, y, 20)

                case _:
                    pass
            continue
        else:
            y += 40

        create_label(main_frame, labeltext, 15, x, y, "#343434")
        match labeltext:
            case "Name of Child*":
                first_name_obj = create_entry(main_frame, first_name_entry, 250, y, 20)
                first_name_obj.focus_set()
                create_entry(main_frame, last_name_entry, 400, y, 25)

            case "Date of Birth*":
                day_combo_box = create_combo_box(main_frame, 250, y, days, 4)
                month_combo_box = create_combo_box(main_frame, 310, y, months, 10)
                year_combo_box = create_combo_box(main_frame, 410, y, years, 5)

            case "Birth Weight*":
                create_entry(main_frame, Birth_Weight_entry, 250, y, 35)

            case "Head circumference":
                create_entry(main_frame, Head_circumference_entry, 250, y, 25)

            case "Delivery":
                create_entry(main_frame, Delivery_entry, 250, y, 80)

            case "Neonatal Status":
                create_entry(main_frame, Neonatal_Status_entry, 250, y, 80)

            case "Blood Group":
                blood_combo_box = create_combo_box(
                    main_frame, 250, y, blood_group_list, 4
                )

            case "Remarks":
                create_entry(main_frame, Remarks_entry, 250, y, 80)

            case "Name of Mother*":
                create_entry(main_frame, Name_of_Mother_entry, 250, y, 80)

            case "Mother's Blood Group":
                mother_blood_combo_box = create_combo_box(
                    main_frame, 250, y, blood_group_list, 4
                )

            case "Name of Father*":
                create_entry(main_frame, Name_of_Father_entry, 250, y, 80)

            case "Father of Blood Group":
                father_blood_combo_box = create_combo_box(
                    main_frame, 250, y, blood_group_list, 4
                )

            case "Details of Siblings":
                create_entry(main_frame, Details_of_Siblings_entry, 250, y, 80)

            case "Phone no.*":
                create_entry(main_frame, Phone_no_entry, 250, y, 80)

            case _:
                pass

    ttk.Button(
        main_frame,
        text="Search",
        width=10,
        command=lambda: search_window_function(
            main_window,
            first_name_entry.get().strip(),
            last_name_entry.get().strip(),
            gender_radio_button.get().strip(),
            day_combo_box.get().strip()
            + " "
            + month_combo_box.get().strip()
            + " "
            + year_combo_box.get().strip(),
        ),
    ).place(x=250, y=690)
    ttk.Button(
        main_frame,
        text="Add new baby",
        width=17,
        command=lambda: add_new_baby(
            main_window,
            first_name_entry.get().strip(),
            last_name_entry.get().strip(),
            gender_radio_button.get(),
            day_combo_box.get().strip()
            + " "
            + month_combo_box.get().strip()
            + " "
            + year_combo_box.get().strip(),
            Delivery_entry.get().strip(),
            Neonatal_Status_entry.get().strip(),
            Birth_Weight_entry.get().strip(),
            Length_entry.get().strip(),
            Head_circumference_entry.get().strip(),
            Chest_circumference_entry.get().strip(),
            blood_combo_box.get().strip(),
            Remarks_entry.get().strip(),
            Name_of_Mother_entry.get().strip(),
            mother_blood_combo_box.get().strip(),
            Name_of_Father_entry.get().strip(),
            father_blood_combo_box.get().strip(),
            Details_of_Siblings_entry.get().strip(),
            Phone_no_entry.get().strip(),
        ),
    ).place(x=500, y=690)
    ttk.Button(
        main_frame,
        text="Clear",
        width=10,
        command=lambda: clear(
            first_name_obj,
            first_name_entry,
            last_name_entry,
            gender_radio_button,
            day_combo_box,
            month_combo_box,
            year_combo_box,
            Delivery_entry,
            Neonatal_Status_entry,
            Birth_Weight_entry,
            Length_entry,
            Head_circumference_entry,
            Chest_circumference_entry,
            blood_combo_box,
            Remarks_entry,
            Name_of_Mother_entry,
            mother_blood_combo_box,
            Name_of_Father_entry,
            father_blood_combo_box,
            Details_of_Siblings_entry,
            Phone_no_entry,
        ),
    ).place(x=550, y=50)
    ttk.Button(
        main_frame, text="Close", width=10, command=lambda: close(main_window)
    ).place(x=650, y=50)

    main_window.bind(
        "<Control-s>",
        lambda event: search_window_function(
            main_window,
            first_name_entry.get().strip(),
            last_name_entry.get().strip(),
            gender_radio_button.get().strip(),
            day_combo_box.get().strip()
            + " "
            + month_combo_box.get().strip()
            + " "
            + year_combo_box.get().strip(),
        ),
    )
    main_window.bind(
        "<Control-a>",
        lambda event: add_new_baby(
            main_window,
            first_name_entry.get().strip(),
            last_name_entry.get().strip(),
            gender_radio_button.get(),
            day_combo_box.get().strip()
            + " "
            + month_combo_box.get().strip()
            + " "
            + year_combo_box.get().strip(),
            Delivery_entry.get().strip(),
            Neonatal_Status_entry.get().strip(),
            Birth_Weight_entry.get().strip(),
            Length_entry.get().strip(),
            Head_circumference_entry.get().strip(),
            Chest_circumference_entry.get().strip(),
            blood_combo_box.get().strip(),
            Remarks_entry.get().strip(),
            Name_of_Mother_entry.get().strip(),
            mother_blood_combo_box.get().strip(),
            Name_of_Father_entry.get().strip(),
            father_blood_combo_box.get().strip(),
            Details_of_Siblings_entry.get().strip(),
            Phone_no_entry.get().strip(),
        ),
    )
    main_window.bind(
        "<Control-c>",
        lambda event: clear(
            first_name_obj,
            first_name_entry,
            last_name_entry,
            gender_radio_button,
            day_combo_box,
            month_combo_box,
            year_combo_box,
            Delivery_entry,
            Neonatal_Status_entry,
            Birth_Weight_entry,
            Length_entry,
            Head_circumference_entry,
            Chest_circumference_entry,
            blood_combo_box,
            Remarks_entry,
            Name_of_Mother_entry,
            mother_blood_combo_box,
            Name_of_Father_entry,
            father_blood_combo_box,
            Details_of_Siblings_entry,
            Phone_no_entry,
        ),
    )
    main_window.bind("<Control-x>", lambda event: close(main_window))

    ttk.Label(
        main_frame, text="* fields - compulsory for adding new baby", width=50
    ).place(x=500, y=720)
    ttk.Label(
        main_frame, text="Name, Gender, DOB - compulsory for Search", width=40
    ).place(x=250, y=720)


def draw_bg_image(main_window):
    # Create a frame
    image_frame = tk.Frame(main_window, bg="blue", width=640, height=750, bd=5)
    image_frame.place(x=50, y=20)

    image_path = "image/baby.jpg"  # Replace with your image path
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)
    background_label = ttk.Label(image_frame, image=photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    background_label.image = photo


def disable_event():
    pass


def start_screen():
    # declare main_window object
    main_window = tk.Tk()
    main_window.state("zoomed")
    main_window.title("Immunization & Health Record")
    main_window.resizable(False, False)
    main_window.protocol("WM_DELETE_WINDOW", disable_event)

    # draw baby image at background
    draw_bg_image(main_window)

    # render first screen
    main_screen(main_window)

    main_window.mainloop()


if __name__ == "__main__":
    start_screen()
