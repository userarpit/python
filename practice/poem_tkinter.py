import tkinter as tk
import random
from tkinter import filedialog


def are_unique(data):
    unique_list = []
    for word in data:
        if word.strip() not in unique_list:
            unique_list.append(word)

    return len(data) == len(unique_list)


def check_count(data):
    count_word = 0
    for word in data:
        if len(word.strip()) > 0:
            count_word += 1

    return count_word


def generate_poem():

    lbl_text["text"] = ""
    nouns = ent_nouns.get().split(",")
    verbs = ent_verbs.get().split(",")
    adjectives = ent_adjectives.get().split(",")
    prepositions = ent_preposition.get().split(",")
    adverbs = ent_adverbs.get().split(",")

    if not (
        are_unique(nouns)
        and are_unique(verbs)
        and are_unique(adjectives)
        and are_unique(prepositions)
        and are_unique(adverbs)
    ):

        lbl_text["text"] = "Please do not enter duplicates words"
        return

    if (
        check_count(nouns) < 3
        or check_count(verbs) < 3
        or check_count(adjectives) < 3
        or check_count(prepositions) < 2
        or check_count(adverbs) < 1
    ):
        lbl_text["text"] = (
            "Please enter at least\n 3 nouns, \n"
            "3 verbs,\n 3 adjectives,\n 2 prepositions,\n and an adverb "
        )
        return

    noun1, noun2, noun3 = random.sample(nouns, k=3)

    verb1, verb2, verb3 = random.sample(verbs, k=3)
    adj1, adj2, adj3 = random.sample(adjectives, k=3)
    prep1, prep2 = random.sample(prepositions, k=2)
    adverb1 = random.choice(adverbs)

    vowel = ["a", "e", "i", "o", "u"]

    lbl_text["text"] = (
        f"{'An' if noun1[0] in vowel else 'A'} {adj1} {noun1} \n\nA {adj1} {noun1} {verb1} {prep1} the {adj2} {noun2} \n{adverb1}, the {noun1} {verb2} \nthe {noun2} {verb3} {prep2} a {adj3} {noun3}"
    )

    return


def save_poem():
    type_list = [("Text files", "*.txt")]
    file_name = filedialog.asksaveasfilename(
        filetypes=type_list, defaultextension="*.txt"
    )

    if file_name is not None:
        with open(file_name, mode="w") as output_file:
            output_file.writelines(lbl_text["text"])


window = tk.Tk()
window.title("Make your own poem")

window.resizable(height=False, width=False)

# header frame
frm_header = tk.Frame(master=window)
lbl_heading = tk.Label(
    master=frm_header,
    text="Enter your favorite words, separated by commas.",
    borderwidth=0,
    relief="raised",
)
lbl_heading.pack(pady=10)
frm_header.pack(padx=5, pady=5)

# label and entry frame

frm_input = tk.Frame(master=window)

lbl_nouns = tk.Label(master=frm_input, text="Nouns:")
lbl_nouns.grid(row=0, column=0, sticky="e")
ent_nouns = tk.Entry(master=frm_input, width=100)
ent_nouns.grid(row=0, column=1, sticky="w")

lbl_verbs = tk.Label(master=frm_input, text="Verbs:")
lbl_verbs.grid(row=1, column=0, sticky="e")
ent_verbs = tk.Entry(master=frm_input, width=100)
ent_verbs.grid(row=1, column=1, sticky="w")

lbl_adjectives = tk.Label(master=frm_input, text="Adjectives:")
lbl_adjectives.grid(row=2, column=0, sticky="e")
ent_adjectives = tk.Entry(master=frm_input, width=100)
ent_adjectives.grid(row=2, column=1, sticky="w")

lbl_preposition = tk.Label(master=frm_input, text="Prepositions:")
lbl_preposition.grid(row=3, column=0, sticky="e")
ent_preposition = tk.Entry(master=frm_input, width=100)
ent_preposition.grid(row=3, column=1, sticky="w")

lbl_adverbs = tk.Label(master=frm_input, text="Adverbs:")
lbl_adverbs.grid(row=4, column=0, sticky="e")
ent_adverbs = tk.Entry(master=frm_input, width=100)
ent_adverbs.grid(row=4, column=1, sticky="w")

frm_input.pack(padx=5, pady=5)

# generate frame
frm_generate = tk.Frame(master=window)
btn_generate = tk.Button(master=frm_generate, text="Generate", command=generate_poem)
btn_generate.pack()
frm_generate.pack(padx=5, pady=5)

# poem frame
frm_poem = tk.Frame(master=window, borderwidth=5, relief="groove")
frm_poem.pack(padx=5, pady=5, fill=tk.X)

lbl_title = tk.Label(master=frm_poem)
lbl_title["text"] = "Your poem:"
lbl_title.pack(pady=10)

lbl_text = tk.Label(master=frm_poem)
lbl_text["text"] = "Press the 'Generate' button to display the poem"
lbl_text.pack(pady=10)

btn_save = tk.Button(master=frm_poem)
btn_save["text"] = "Save to file"
btn_save["command"] = save_poem
btn_save.pack(pady=10)

window.mainloop()
