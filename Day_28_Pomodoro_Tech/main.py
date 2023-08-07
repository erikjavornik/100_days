from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


# ---------------------------- UI SETUP ------------------------------- #
#Window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

def function(arg):
    print(arg)
    
window.after(1000, )

#Start Button
start_button = Button(text="Start")
start_button.grid(column=0, row=3)
#Reset Button
reset_button = Button(text="Reset")
reset_button.grid(column=3, row=3)
#Timer Label
timer_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"), bg=YELLOW)
timer_label.grid(column=1,row=1)
#Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="./Day_28_Pomodoro_Tech/tomato.png")
canvas.create_image(103, 112, image=tomato_img)
canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=2)

window.mainloop()