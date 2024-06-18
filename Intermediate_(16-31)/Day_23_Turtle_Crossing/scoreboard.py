FONT = ("Courier", 24, "normal")

from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.level += 1
        self.clear()
        
        self.goto(-200, 250)
        self.write(f"Level: {self.level}", align="center", font=FONT)
        
    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg=f"Game Over!", align= "center", font=FONT)
