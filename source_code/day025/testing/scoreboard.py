from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 360)
        self.player1score = 0
        self.player2score = 0
        self.update()

    def player1(self):
        self.player1score += 1
        self.update()

    def player2(self):
        self.player2score += 1
        self.update()

    def update(self):
        self.clear()
        self.write(f"{self.player1score}   {self.player2score}",
                   False, align="center", font=("Agency FB", 48, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, align="center",
                   font=("Agency FB", 48, "bold"))
