from tkinter import (
    Tk,
    Button,
    PhotoImage,
    Canvas,
)

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="images/card_front.png")
canvas.grid(row=0, column=0, columnspan=2)

canvas.create_image(400, 263, image=card_front_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

canvas.create_text(400, 150, text="Title", font=("Ariel", 48, "italic"))
canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))


right_button_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_image, highlightthickness=0)
right_button.grid(row=1, column=0)
wrong_button_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_image, highlightthickness=0)
wrong_button.grid(row=1, column=1)

window.mainloop()

