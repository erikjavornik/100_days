from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        #Window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        #Score board Label
        self.score_board = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_board.config(pady=20)
        self.score_board.grid(column=2, row=1)

        #Canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        
        self.canvas.grid(column=1, row=2, columnspan=2, pady=50)

        self.question_text = self.canvas.create_text(
            150,
            125, 
            text="Placeholder", 
            font=("Arial", 20, "italic"), 
            fill=THEME_COLOR,
            width=280
        )

        #True Button
        self.true_image = PhotoImage(file="./Day_34_Quizzler_App/quizzler-app-start/images/true.png")
        self.true_button = Button(image=self.true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(column=1, row=3)
        #False Button 
        self.false_image = PhotoImage(file="./Day_34_Quizzler_App/quizzler-app-start/images/false.png")
        self.false_button = Button(image=self.false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(column=2, row=3)

        self.get_next_question()

        self.window.mainloop()
    
    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right == True:
            self.canvas.config(bg="Green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_board.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="End of Quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")