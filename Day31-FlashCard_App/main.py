from tkinter import *
import pandas, random

BACKGROUND_COLOR = "#B1DDC6"

# ##################### ADD THE FLASH CARD FUNCTIONALITY ##############
current_card = {}
to_learn = {}

try:
	data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
	original_data = pandas.read_csv("data/french_words.csv")
	to_learn = original_data.to_dict(orient="records")
else:
	to_learn = data.to_dict(orient="records")


def new_card():
	global current_card, flash_card
	window.after_cancel(flash_card)
	current_card = random.choice(to_learn)
	canvas.itemconfig(lang_text, text="French", fill="black")
	canvas.itemconfig(word_text, text=current_card["French"], fill="black")
	canvas.itemconfig(canvas_image, image=card_front)
	flash_card = window.after(3000, flip_card)


def flip_card():
	canvas.itemconfig(canvas_image, image=card_back)
	canvas.itemconfig(lang_text, text="English", fill="white")
	canvas.itemconfig(word_text, text=current_card["English"], fill="white")

def known_word():
	to_learn.remove(current_card)
	new_data = pandas.DataFrame(to_learn)
	new_data.to_csv("data/words_to_learn.csv", index=False)
	new_card()

# ###################### UI SETUP #####################################

window = Tk()
window.title("FlashCard App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flash_card = window.after(3000, flip_card)

card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
ok_image = PhotoImage(file="images/right.png")
x_image = PhotoImage(file="images/wrong.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(400, 263, image=card_front)
lang_text = canvas.create_text(400, 150, text="Title", fill="black", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="word", fill="black", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

ok_button = Button(image=ok_image, command=known_word, highlightthickness=0, borderwidth=0, bg=BACKGROUND_COLOR, width=96, height=96)
ok_button.grid(row=1, column=1)

x_button = Button(image=x_image, command=new_card, highlightthickness=0, borderwidth=0, bg=BACKGROUND_COLOR, width=96, height=96)
x_button.grid(row=1, column=0)

new_card()
window.mainloop()
