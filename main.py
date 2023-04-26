from tkinter import *
import pandas
import random
#---------------------------------------------NEW FLASH CARDS----------------------------------------------------------#

current_card = {}
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
finally:
    word_list = data.to_dict(orient='records')



def random_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(word_list)
    canvas.itemconfig(card_word, text=current_card["French"], fill="Black")
    canvas.itemconfig(card_title, text="French", fill="Black")
    canvas.itemconfig(canvas_image, image=front_logo)
    flip_timer = window.after(3000, func=flip_card)

def got_word_right():
    print(len(word_list))
    word_list.remove(current_card)
    data = pandas.DataFrame(word_list)
    data.to_csv("data/words_to_learn.csv")

    random_word()





def flip_card():
    canvas.itemconfig(canvas_image, image=back_logo)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")

#----------------------------------------------------UI----------------------------------------------------------------#

BACKGROUND_COLOR = "#B1DDC6"
FONT = ("Ariel", 40, "italic")
window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("Flashy")
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_logo = PhotoImage(file="images/card_front.png")
back_logo = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_logo)
canvas.grid(row=0, column=0, columnspan=2)
card_title = canvas.create_text(400, 150, text="", font=FONT)
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 40, "bold"))

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=got_word_right)
right_button.grid(row=1, column=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=random_word)
wrong_button.grid(row=1, column=0)

random_word()


window.mainloop()