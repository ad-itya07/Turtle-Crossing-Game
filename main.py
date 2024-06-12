import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Cross The Road!!")
screen.tracer(0)
screen.listen()

player = Player()
scoreboard = Scoreboard()
cars = CarManager()

screen.onkeypress(fun=player.move, key="Up")

cnt_loop = 0
game_is_on = True
while game_is_on:
    cnt_loop += 1
    time.sleep(0.1)
    screen.update()

    if cnt_loop % cars.cars_in_second == 0:
        cars.create_car()

    cars.move()

#     DETECTING COLLISION WITH CARS:
    for car in cars.cars_list:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

    #  DETECTING LEVEL COMPLETION
    if player.ycor() >= 280:
        # cars.cars_in_second *= 0.9
        player.level_up()
        cars.level_up()
        scoreboard.level_up()

screen.exitonclick()