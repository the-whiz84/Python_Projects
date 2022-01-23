import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

player = Player()
screen = Screen()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.setup(width=1000, height=800)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.finish_line():
        scoreboard.increase_level()
        car_manager.level_up()

screen.exitonclick()
