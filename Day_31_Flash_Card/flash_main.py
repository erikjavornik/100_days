from tkinter import *
import random
import pandas

# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
START_LANGUAGE = "Kanji"
TRANS_LANGUAGE = "English"
FONT = "Arial"

# ---------------------------- FIND/CREATE DATA LIST ------------------------------- #
#Depending on if file exists, change where data is being pulled from 
try:
    data = pandas.read_csv("./Day_31_Flash_Card/data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./Day_31_Flash_Card/data/kanji - Sheet1.csv")

data_dict = data.to_dict(orient="records")

# ---------------------------- WORD GENERATOR ------------------------------- #
#Front of card 
def display_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    #Modify front of card
    flash_card.itemconfig(canvas_image, image=card_front_img)
    flash_card.itemconfig(language_text, fill= "black", text = START_LANGUAGE)
    flash_card.itemconfig(word_text, fill= "black", text=current_card["Jap Kanji"])
    #3 sec timer to flip to back of card
    flip_timer = window.after(3000, func=flip_card)
#Flip to back of card
def flip_card():
    flash_card.itemconfig(canvas_image, image=card_back_img)
    flash_card.itemconfig(language_text, fill= "white", text = TRANS_LANGUAGE)
    flash_card.itemconfig(word_text, fill= "white", text=current_card["English"])
#Remove known words from list of possible words
def is_known():
    data_dict.remove(current_card)
    to_learn = pandas.DataFrame(data_dict)
    #Export words still need top learn so user can pick up where they left off
    to_learn.to_csv("./Day_31_Flash_Card/data/words_to_learn.csv", index=False)
    display_word()
# ---------------------------- UI SETUP ------------------------------- #
#Window
window = Tk()
window.title("Kanji Flash Cards")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, func=flip_card)
#Check Button
check_image = PhotoImage(file="./Day_31_Flash_Card/images/right.png")
check_button = Button(image=check_image, highlightthickness=0, command=is_known)
check_button.grid(column=1, row=1)
#X Button
x_image = PhotoImage(file="./Day_31_Flash_Card/images/wrong.png")
x_button = Button(image=x_image, highlightthickness=0, command=display_word)
x_button.grid(column=0, row=1)
#Flash Card as a canvas
flash_card = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="./Day_31_Flash_Card/images/card_front.png")
card_back_img = PhotoImage(file="./Day_31_Flash_Card/images/card_back.png")
canvas_image = flash_card.create_image(400, 250, image=card_front_img)
flash_card.grid(column=0, row=0, columnspan=2)

#Creating text on canvas with placeholder text
language_text = flash_card.create_text(400, 150, text="", font=(FONT, 40, "italic"))
word_text = flash_card.create_text(400, 263, text="", font=(FONT, 60, "bold"))

#Starting display of word and title
display_word()

window.mainloop()