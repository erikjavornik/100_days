from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 15

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.reset()

    def up(self):
        self.forward(MOVE_DISTANCE)
    
    def reset(self):
        self.goto(STARTING_POSITION)