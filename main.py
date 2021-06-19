from tkinter import (
    Tk,
    Button,
    PhotoImage,
    Canvas,
)
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"


def load_questions():
    csv_content = pd.read_csv("data/french_words.csv")
    return pd.DataFrame(csv_content)


def generate_new_word():
    word_pair = questions.sample()
    french_word = word_pair["French"].values[0]
    canvas.itemconfig(french_word_display_id, text=french_word)


questions = load_questions()

window = Tk()
window.title("Flash cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="images/card_front.png")
canvas.grid(row=0, column=0, columnspan=2)

canvas.create_image(400, 263, image=card_front_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

canvas.create_text(400, 150, text="French", font=("Ariel", 48, "italic"))
french_word_display_id = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))

right_button_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_image, highlightthickness=0, command=generate_new_word)
right_button.grid(row=1, column=0)
wrong_button_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_image, highlightthickness=0, command=generate_new_word)
wrong_button.grid(row=1, column=1)

generate_new_word()

window.mainloop()

