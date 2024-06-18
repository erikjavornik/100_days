import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_INCREMENT = 10
START_X = 300

class CarManager():
    def __init__(self):
        self.car_list = []
        self.new_move_distance = 5 
    
    def car_move(self):
        for car in self.car_list:
            car.backward(self.new_move_distance)
        
    def increase_speed(self):
        self.new_move_distance += MOVE_INCREMENT
        
    def create_car(self):
        new_car = Turtle()
        new_car.shape("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.color(random.choice(COLORS))
        y_cord = random.randint(-250, 250)
        new_car.goto(START_X, y_cord)
        self.car_list.append(new_car)