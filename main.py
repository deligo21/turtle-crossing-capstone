import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkeypress(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car_manager.createCars()
    car_manager.move()
    
    for car in car_manager.all_cars:
        if car.distance(player) < 25:
            scoreboard.game_over()
            game_is_on = False
    
    if player.ycor() > 280:
        player.new_level()
        scoreboard.update_scoreboard()
        car_manager.increase_speed()
        
screen.exitonclick()
