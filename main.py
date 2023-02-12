from tkinter import *
from random import choice

# ---------------------------- FLIPPING CARDS ------------------------------- #
lang = 1


def flip():
    global card
    global lang

    if lang == 2:
        # switch to Deutsche card
        card.config(file="Rounded Rectangle 2.png")
        lang = 1
    else:
        # switch to English card
        card.config(file="Rounded Rectangle 1.png")
        lang = 2


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.minsize(width=400, height=400)
window.config(padx=50, pady=50, background="#3944Bc")

card = PhotoImage(file="Rounded Rectangle 2.png")
card_canvas = Canvas(width=550, height=400, highlightthickness=0, background="#3944Bc")
card_canvas.create_image(275, 200, image=card)
card_canvas.grid(row=0, column=0, columnspan=3)

# Buttons
tick_mark = PhotoImage(file="tick mark.png")
tick_mark_button = Button(image=tick_mark, background="#3944Bc", borderwidth=0,
                          activebackground="#3944Bc")
tick_mark_button.grid(row=1, column=0)

flip_pic = PhotoImage(file="flip pic.png")
flip_button = Button(image=flip_pic, background="#3944Bc", borderwidth=0,
                     activebackground="#3944Bc", command=flip)
flip_button.grid(row=1, column=1)

cross_mark = PhotoImage(file="cross mark.png")
cross_mark_button = Button(image=cross_mark, background="#3944Bc", borderwidth=0,
                           activebackground="#3944Bc")
cross_mark_button.grid(row=1, column=2)

window.mainloop()
