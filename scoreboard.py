FONT = ("Courier", 20, "normal")

from turtle import Turtle
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(x=-280,y=250)
        self.write(arg=f"Level : {self.level}",align="left",font=FONT)

    def game_over(self):
        self.home()
        self.write(arg="GAME OVER",align="center",font=FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.write(arg=f"Level : {self.level}",align="left",font=FONT)

