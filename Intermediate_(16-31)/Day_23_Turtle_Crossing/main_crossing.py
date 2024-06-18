import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

FINISH_LINE_Y = 280

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")

counter = 6

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    #Create a New car obstical every 6th loop
    if counter % 6 == 0:
        car_manager.create_car()
    
    car_manager.car_move()
    
    #Determine if player reached the finish line
    if player.ycor() > FINISH_LINE_Y:
        player.reset()
        car_manager.increase_speed()
        scoreboard.update_scoreboard()
    
    #Detect if a car hit the player    
    for car in car_manager.car_list:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()
    
    #Increase loop counter
    counter += 1
screen.exitonclick()