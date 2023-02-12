from tkinter import *


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.minsize(width=400, height=400)
window.config(padx=50, pady=50, background="#3944Bc")

english_card = PhotoImage(file="Rounded Rectangle 1.png")
english_card_canvas = Canvas(height=400, width=550, highlightthickness=0, background="#3944Bc")
english_card_canvas.create_image(275, 200, image=english_card)
english_card_canvas.grid(row=0, column=0, columnspan=2)

deutsche_card = PhotoImage(file="Rounded Rectangle 2.png")
deutsche_card_canvas = Canvas(height=400, width=550, highlightthickness=0, background="#3944Bc")
deutsche_card_canvas.create_image(275, 200, image=deutsche_card)
deutsche_card_canvas.grid(row=0, column=0, columnspan=2)

tick_mark = PhotoImage(file="tick mark.png")
tick_mark_button = Button(image=tick_mark, background="#3944Bc", borderwidth=0, activebackground="#3944Bc")
tick_mark_button.grid(row=1, column=0)

cross_mark = PhotoImage(file="cross mark.png")
cross_mark_button = Button(image=cross_mark, background="#3944Bc", borderwidth=0, activebackground="#3944Bc")
cross_mark_button.grid(row=1, column=1)

window.mainloop()
