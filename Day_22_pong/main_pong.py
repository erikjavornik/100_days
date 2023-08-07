from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

SCREEN_W = 800
SCREEN_H = 600

screen = Screen()


#Setup screen
screen.bgcolor("black")
screen.setup(width=SCREEN_W, height=SCREEN_H)
screen.title("PONGGGGGGGGG!")
screen.tracer(0)

r_paddle = Paddle(350)
l_paddle = Paddle(-350)

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    
    ball.move()
    
    #Detect collision with wall    
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        
    #Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect if R paddle missed
    if ball.xcor() > 390: 
        ball.reset()
        scoreboard.l_point()
        
    #Detect if L paddle missed
    if ball.xcor() < -390:
        ball.reset()
        scoreboard.r_point()
        
screen.exitonclick()