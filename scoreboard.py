from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.change_score()

    def inc_score(self):
        self.score += 1
        self.change_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER")
    def change_score(self):
        self.clear()
        self.write(f"Score: {self.score}")
