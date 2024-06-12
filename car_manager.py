COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CARS_IN_SECOND = 6

from turtle import Turtle
import random


class CarManager():

    def __init__(self):
        self.cars_list = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.cars_in_second = CARS_IN_SECOND

    def create_car(self):
        new_car = Turtle()
        new_car.shape("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.goto(x=280, y=random.randint(-250, 250))
        new_car.color(random.choice(COLORS))
        self.cars_list.append(new_car)


    def move(self):
        for car in self.cars_list:
            new_x = car.xcor() - self.car_speed
            car.goto(new_x,car.ycor())


    def level_up(self):
        self.car_speed += MOVE_INCREMENT
