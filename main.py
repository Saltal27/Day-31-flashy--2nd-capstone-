import random
from tkinter import *
import pandas
import json


# ---------------------------- RESET DICTIONARY ------------------------------- #
def reset_dict():
    raw_data = pandas.read_csv("resources/1000 most common words.csv")
    with open("data.json", "w") as raw_data_file:
        json.dump(raw_data.to_dict(), raw_data_file, indent=4)


# ---------------------------- PICKING WORDS ------------------------------- #
word_index = 0


def random_pick():
    global word_index
    global lang
    picking = True

    while picking:
        word_index = random.randint(0, 999)
        try:
            with open("data.json") as data_file:
                data = json.load(data_file)
                if lang == 1:
                    card_word.config(text=data["Deutsche"][f"{word_index}"])
                else:
                    card_word.config(text=data["English"][f"{word_index}"])
        except KeyError:
            pass
        else:
            picking = False


# ---------------------------- TICK ------------------------------- #
def tick():
    with open("data.json") as data_file:
        data = json.load(data_file)
        del data["Deutsche"][f"{word_index}"]
        del data["English"][f"{word_index}"]

    with open("data.json", "w") as data_file:
        json.dump(data, data_file, indent=4)

    random_pick()


# ---------------------------- FLIPPING CARDS ------------------------------- #
lang = 1


def flip():
    global card
    global lang

    if lang == 2:
        # switch to Deutsche card
        card.config(file="images/Rounded Rectangle 2.png")
        with open("data.json") as data_file:
            data = json.load(data_file)
            card_word.config(text=data["Deutsche"][f"{word_index}"])
        lang = 1
    else:
        # switch to English card
        card.config(file="images/Rounded Rectangle 1.png")
        with open("data.json") as data_file:
            data = json.load(data_file)
            card_word.config(text=data["English"][f"{word_index}"])
        lang = 2


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.minsize(width=400, height=400)
window.config(padx=50, pady=50, background="#3944Bc")

card = PhotoImage(file="images/Rounded Rectangle 2.png")
card_canvas = Canvas(width=550, height=400, highlightthickness=0, background="#3944Bc")
card_canvas.create_image(275, 200, image=card)
card_canvas.grid(row=0, column=0, columnspan=3)

# Buttons
tick_mark = PhotoImage(file="images/tick mark.png")
tick_mark_button = Button(image=tick_mark, background="#3944Bc", borderwidth=0,
                          activebackground="#3944Bc", command=tick)
tick_mark_button.grid(row=1, column=0)

flip_pic = PhotoImage(file="images/flip pic.png")
flip_button = Button(image=flip_pic, background="#3944Bc", borderwidth=0,
                     activebackground="#3944Bc", command=flip)
flip_button.grid(row=1, column=1)

cross_mark = PhotoImage(file="images/cross mark.png")
cross_mark_button = Button(image=cross_mark, background="#3944Bc", borderwidth=0,
                           activebackground="#3944Bc", command=random_pick)
cross_mark_button.grid(row=1, column=2)

reset_pic = PhotoImage(file="images/reset pic.png")
reset = Button(image=reset_pic, background="#3944Bc", borderwidth=0,
               activebackground="#3944Bc", command=reset_dict)
reset.grid(row=2, column=1)

# Labels
card_word = Label(text="", font=("Arial Rounded MT", 30, "bold"), foreground="#3944Bc", background="white")
card_word.grid(row=0, column=0, columnspan=3)
random_pick()

window.mainloop()
