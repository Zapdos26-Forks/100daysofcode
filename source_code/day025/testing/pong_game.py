from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard


class PongGame:
    def __init__(self):
        self.running = True

        self.screen = Screen()
        self.screen.setup(width=900, height=900)
        self.boundaries = {
            "ceiling": self.screen.window_height() // 2 - 60,
            "right_wall": self.screen.window_width() // 2 - 30,
            "floor": self.screen.window_height() // -2 + 60,
            "left_wall": self.screen.window_width() // -2 + 30
        }

        self.player1 = Paddle("left", self.boundaries)
        self.player2 = Paddle("right", self.boundaries)

        self.ball = Ball(self.boundaries, (self.player1, self.player2))

        self.scoreboard = Scoreboard()

        self.screen.onkeypress(self.player1.move_up, "w")
        self.screen.onkeypress(self.player1.move_down, "s")
        self.screen.onkeypress(self.player2.move_up, "Up")
        self.screen.onkeypress(self.player2.move_down, "Down")
        self.screen.onkeyrelease(self.player1.stop, "w")
        self.screen.onkeyrelease(self.player1.stop, "s")
        self.screen.onkeyrelease(self.player2.stop, "Up")
        self.screen.onkeyrelease(self.player2.stop, "Down")
        self.screen.listen()

    def run(self):
        self.player1.tick()
        self.player2.tick()
        self.

        if self.ball.xcor()-1 <= self.boundaries["left_wall"]:
            self.scoreboard.player2()
            self.ball.start_over()
        elif self.ball.xcor()+1 >= self.boundaries["right_wall"]:
            self.scoreboard.player1()
            self.ball.start_over()
        elif (self.ball.ycor() >= self.boundaries["ceiling"] or
                self.ball.ycor() <= self.boundaries["floor"]):
            self.ball.y_direction *= -1
        elif self.ball.xcor() < 0:
            player_x, player_y = self.player1.position()
            if self.ball.xcor() <= player_x and self.ball.ycor() <= player_y + 69 and self.ball.ycor() >= player_y - 69:
                self.ball.x_direction *= -1
        else:
            player_x, player_y = self.player2.position()
            if self.ball.xcor() >= player_x and self.ball.ycor() <= player_y + 69 and self.ball.ycor() >= player_y - 69:
                self.ball.x_direction *= -1

        if self.scoreboard.player1score >= 3 or self.scoreboard.player2score >= 3:
            self.scoreboard.game_over()
            self.running = False

        if self.running:
            self.screen.ontimer(self.run, 1)
