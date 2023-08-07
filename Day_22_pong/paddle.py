from turtle import Turtle

PAD_HEADING = 90
Y_START = 0
MOVE_DISTANCE = 20

class Paddle(Turtle):
    def __init__(self, start_x):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len= 5)
        self.setheading(PAD_HEADING)
        self.goto(x=start_x, y=Y_START)
    
    def up(self):
        self.forward(MOVE_DISTANCE)
    
    def down(self):
        self.backward(MOVE_DISTANCE)
        