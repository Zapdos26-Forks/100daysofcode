from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, side, boundaries):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=6)
        self.setheading(90)
        self.is_moving = False
        self.direction = None
        if side == "left":
            self.setx(-400)
        else:
            self.setx(400)
        self.ceiling = boundaries["ceiling"]
        self.floor = boundaries["floor"]

    def tick(self):
        if self.is_moving:
            if self.direction == self.forward and self.ycor() < self.ceiling:
                self.direction(25)
            if self.direction == self.backward and self.ycor() > self.floor:
                self.direction(25)

    def move_up(self):
        self.is_moving = True
        self.direction = self.forward

    def move_down(self):
        self.is_moving = True
        self.direction = self.backward

    def stop(self):
        self.is_moving = False
