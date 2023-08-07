from turtle import Turtle

X_CORD = 0
Y_CORD = 260
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
        
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=X_CORD, y=Y_CORD)
        self.score_refresh()
        
        
    def increase_score(self):
        self.score += 1
        self.score_refresh()
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.score_refresh()
            
    # def game_over(self):
    #     self.goto(x=0, y=0)
    #     self.write(arg=f"Game Over!", align= ALIGNMENT, font=FONT)
    
    def score_refresh(self):
        self.clear()
        self.write(arg=f"Score: {self.score}  High Score: {self.high_score}", align= ALIGNMENT, font=FONT)