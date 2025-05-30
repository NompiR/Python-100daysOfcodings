from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data_file = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data_file.to_dict(orient="records")



def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    #print(current_card['French'])
    canvas.itemconfig(card_title, text='French', fill="black")
    canvas.itemconfig(card_word, text=current_card['French'], fill="black")
    canvas.itemconfig(canvas_image, image=image_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card['English'], fill="white")
    canvas.itemconfig(canvas_image, image=image_back)

def unknown_word():
    to_learn.remove(current_card)

    #unknown_word_dict = [{'French': current_card['French'], 'English': current_card['English']}]
    #print(unknown_word_dict)
    # df = pandas.DataFrame(data=to_learn)
    # df.loc[len(df)] = unknown_word_dict
    # print(df)

    print(len(to_learn))
    df= pandas.DataFrame(data=to_learn)
    df.to_csv("data/words_to_learn.csv", index=False)
    next_card()



window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
image_front = PhotoImage(file="images/card_front.png")
image_back = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=image_front)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial",60, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, bg=BACKGROUND_COLOR, border=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, bg=BACKGROUND_COLOR, border=0, command=unknown_word)
known_button.grid(row=1, column= 1)


next_card()


window.mainloop()
