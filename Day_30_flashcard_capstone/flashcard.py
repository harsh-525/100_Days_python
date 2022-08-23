from tkinter import *
import pandas as pd
from random import choice

BACKGROUND_COLOR = "#B1DDC6"

# TODO 2: import the french data
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")
data_dict = data.to_dict(orient='records')
current_card = {}

# TODO 3: Generate random french word on click
def generate_fr_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(data_dict)
    word = current_card['French']
    canvas.itemconfig(canvas_image, image=flashcard_front_img)
    canvas.itemconfig(lan_title, text="French")
    canvas.itemconfig(fr_word, text=word)
    flip_timer = window.after(3000, func=flip_en_word)

# TODO 4: Flip to eng word
def flip_en_word():
    word = current_card['English']
    canvas.itemconfig(canvas_image, image=flashcard_back_img)
    canvas.itemconfig(lan_title, text="English")
    canvas.itemconfig(fr_word, text=word)

# TODO 5: seperate known and unknown words
def known_words():
    data_dict.remove(current_card)
    unknown_words = pd.DataFrame(data_dict)
    unknown_words.to_csv("data/words_to_learn.csv", index=False)
    generate_fr_word()

# TODO 1: UI SETUP
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_en_word)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
flashcard_front_img = PhotoImage(file="images/card_front.png")
flashcard_back_img = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=flashcard_front_img)
canvas.grid(column=0, row=0, columnspan=2)

lan_title = canvas.create_text(400, 150, text="Language", font=("Arial", 50, "italic"), fill="black")
fr_word = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"), fill="black")

wrong_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=wrong_img, highlightthickness=0, command=generate_fr_word)
unknown_button.grid(column=0, row=1)

correct_img = PhotoImage(file="images/right.png")
known_button = Button(image=correct_img, highlightthickness=0, command=known_words)
known_button.grid(column=1, row=1)

generate_fr_word()

window.mainloop()



