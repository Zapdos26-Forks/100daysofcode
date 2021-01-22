from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, alignment="center", font=("Courier", 24, "normal")):
        super().__init__()
        self.score = 0
        self.alignment = alignment
        self.font = font
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}",
                   align=self.alignment, font=self.font)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=self.alignment, font=self.font)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
