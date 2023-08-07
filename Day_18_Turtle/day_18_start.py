# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 14:32:34 2023

@author: Erik.Javornik
"""

from turtle import Turtle, Screen

timmy_the_turtle = Turtle()

# #Change turtle attributes
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")

## Draw a square
# for i in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)

# # Draw a dashed line
# for i in range(15):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.up()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.down()

# # Draw overlaying shapes
# import random
# num_sides = 3
# total_angel = 360
# should_loop = True
# color = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

# while should_loop:
#     angel = total_angel/num_sides
#     timmy_the_turtle.pencolor(random.choice(color))
#     for i in range(num_sides):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(angel)
        
#     num_sides += 1
#     if num_sides == 11:
#         should_loop = False
    
## Draw a Random Walk
# import turtle as t
# import random

# t.colormode(255)

# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r, g, b)
#     return random_color
    
# directions = [0, 90, 180, 270]
# t.speed("fastest")
# timmy_the_turtle.pensize(15)

# for i in range (100):
#     timmy_the_turtle.setheading(random.choice(directions))
#     timmy_the_turtle.pencolor(random_color())
#     timmy_the_turtle.forward(30)
# screen = Screen()
# screen.exitonclick()

# Draw a Spirograph
import turtle as t
import random

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

t.speed("fastest")

def draw_spirograph(size_of_gap):
    
    for _ in range(int(360 / size_of_gap)):
        timmy_the_turtle.color(random_color())
        timmy_the_turtle.circle(100)
        timmy_the_turtle.setheading(timmy_the_turtle.heading() + size_of_gap)

draw_spirograph(5)

screen = Screen()
screen.exitonclick()