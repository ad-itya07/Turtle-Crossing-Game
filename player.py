STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.turtle_speed = MOVE_DISTANCE
    def move(self):
        self.forward(self.turtle_speed)

    def level_up(self):
        self.turtle_speed += 2
        self.goto(STARTING_POSITION)




