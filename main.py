from tkinter import (
    Tk,
    Label,
    Button,
    Image,
    PhotoImage,
)

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash cards")
window.config(padx=50, pady=50)

website_label = Label(text="French")
website_label.grid(row=0, column=0, columnspan=2)


website_label = Label(text="word")
website_label.grid(row=1, column=0, columnspan=2)


def create_image_button(image_path):
    image = PhotoImage(image_path, width=100, height=100)
    return Button(image=image)


right_button = create_image_button("right.png")
right_button.grid(row=2, column=0)

window.mainloop()

