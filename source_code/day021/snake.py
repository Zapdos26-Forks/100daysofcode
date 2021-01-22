from turtle import Turtle
import math


class Snake:

    def __init__(self):
        self.segments = []
        self.starting_position = [
            (0, 0), (-20, 0), (-40, 0)]
        self.move_distance = 20
        self.directions = {'up': 90, 'down': 270, 'left': 180, 'right': 0}
        self.create_snake()
        self._head = self.segments[0]

    @property
    def head(self):
        return self._head

    def create_snake(self):
        for position in self.starting_position:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
        self.update_color()

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def update_color(self):
        for i in range(len(self.segments)):
            self.segments[i].color(
                int((math.sin((.3 * i) + 0) * 127) + 127.5),
                int((math.sin((.3 * i) + 2) * 127) + 127.5),
                int((math.sin((.3 * i) + 4) * 127) + 127.5)
            )

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self._head.forward(self.move_distance)

    def up(self):
        if self._head.heading() != self.directions['down']:
            self._head.setheading(self.directions['up'])

    def down(self):
        if self._head.heading() != self.directions['up']:
            self._head.setheading(self.directions['down'])

    def left(self):
        if self._head.heading() != self.directions['right']:
            self._head.setheading((self.directions['left']))

    def right(self):
        if self._head.heading() != self.directions['left']:
            self._head.setheading(self.directions['right'])
