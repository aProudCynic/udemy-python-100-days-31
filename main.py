from tkinter import (
    Tk,
    Button,
    PhotoImage,
    Canvas,
)
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

word_pair = None
current_counter_id = None

window = Tk()
window.title("Flash cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)


def load_questions():
    csv_content = pd.read_csv("data/french_words.csv")
    return pd.DataFrame(csv_content)


def flip_card():
    canvas.itemconfig(language, text="English")
    canvas.itemconfig(canvas_image, image=card_back_image)
    english_word = word_pair["English"].values[0]
    canvas.itemconfig(french_word_display_id, text=english_word, fill="white")


def generate_new_word():
    global current_counter_id
    global word_pair
    if current_counter_id is not None:
        window.after_cancel(current_counter_id)
    word_pair = questions.sample()
    canvas.itemconfig(language, text="French")
    canvas.itemconfig(canvas_image, image=card_front_image)
    french_word = word_pair["French"].values[0]
    canvas.itemconfig(french_word_display_id, text=french_word, fill="black")
    window.after(3000, func=flip_card)


questions = load_questions()

card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
canvas.grid(row=0, column=0, columnspan=2)

canvas_image = canvas.create_image(400, 263, image=card_front_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

french_word_display_id = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
language = canvas.create_text(400, 150, text="French", font=("Ariel", 48, "italic"))

right_button_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_image, highlightthickness=0, command=generate_new_word)
right_button.grid(row=1, column=0)
wrong_button_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_image, highlightthickness=0, command=generate_new_word)
wrong_button.grid(row=1, column=1)

generate_new_word()

window.mainloop()

