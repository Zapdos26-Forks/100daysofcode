from turtle import Turtle
from random import choice, randint
from time import sleep


class Ball(Turtle):
    def __init__(self, boundaries, players):
        super().__init__()
        self.shape("square")
        self.shapesize(1, 1)
        self.penup()
        self.x_speed = 5
        self.y_speed = 5
        self.x_direction = choice([1, -1])
        self.y_direction = choice([1, -1])
        self.boundaries = boundaries
        self.sety(
            randint(self.boundaries["floor"], self.boundaries["ceiling"]))
        self.players = players

    def tick(self):
        x = self.xcor() + (self.x_speed * self.x_direction)
        y = self.ycor() + (self.y_speed * self.y_direction)
        self.goto(x, y)

    def start_over(self):
        self.x_direction = choice([1, -1])
        self.y_direction = choice([1, -1])
        self.setx(0)
        self.sety(
            randint(self.boundaries["floor"], self.boundaries["ceiling"]))
        sleep(3)
