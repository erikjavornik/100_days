from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

FONT_NAME = "Arial"
BOLD = "bold"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    password_input.delete(0, END)
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for char in range(randint(4, 6))]
    password_list += [choice(symbols) for char in range(randint(2, 4))]
    password_list += [choice(numbers) for char in range(randint(2, 4))]

    password = shuffle(password_list)
    password = "".join(password_list)
    
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    email = email_input.get()
    website = website_input.get()
    password = password_input.get()
    
    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?")
    
    if is_ok:
        if len(website) == 0:
            messagebox.showerror(title="Error", message="Fill in website information.")
        elif len(password) == 0:
            messagebox.showerror(title="Error", message="Fill in password.")
        else:
            with open("./Day_29_Password_Manager/Passwords.txt", mode="a") as file:
                file.write(f"{website} | {email} | {password}\n")
            website_input.delete(0, END)
            password_input.delete(0, END)
            website_input.focus()
# ---------------------------- UI SETUP ------------------------------- #
#Window
window = Tk()
window.title("Password Manager")
window.config(width=400, height=400, padx=50, pady=20)
#Canvas
canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="./Day_29_Password_Manager/logo.png")
canvas.create_image(100,100, image=lock_img)
canvas.grid(column=2, row=1)
#Website Label
website_label = Label(text="Website:", font=(FONT_NAME, 10, BOLD))
website_label.grid(column=1,row=2)
#Website Textbox
website_input = Entry()
website_input.grid(column=2, row=2, columnspan=2, sticky="EW")
website_input.focus()
#Email Label
email_label = Label(text="Email/Username:", font=(FONT_NAME, 10, BOLD))
email_label.grid(column=1,row=3)
#Email Textbox
email_input = Entry()
email_input.grid(column=2, row=3, columnspan=2, sticky="EW")
email_input.insert(0, "@gmail.com")
#Password Label
password_label = Label(text="Password:", font=(FONT_NAME, 10, BOLD))
password_label.grid(column=1,row=4)
#Password Textbox
password_input = Entry()
password_input.grid(column=2, row=4, sticky="EW")
#Password Button
password_button = Button(text="Generate Password", command=gen_password)
password_button.grid(column=3, row=4, sticky="EW")
#Add Button
add_button = Button(text="Add", command=save, width=36)
add_button.grid(column=2, row=5, columnspan=2, sticky="EW")

window.mainloop()