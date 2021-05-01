from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.goto(-10, 270)
        self.color("white")
        self.write(f"Score = {self.score} High Score = {self.highscore}", False, align="center",
                   font=("Arial", 16, "normal"))
        self.ht()

    def add_score(self):
        self.score += 1
        self.clear()
        self.goto(0, 270)
        self.write(f"Score = {self.score}", False, align="center", font=("Arial", 16, "normal"))

    def restart_score(self):
        self.score = 0
        self.clear()
        self.goto(-10, 270)
        self.write(f"Score = {self.score}", False, align="center", font=("Arial", 16, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.ht()
        self.color("white")
        self.write("Game Over", False, align="center", font=("Arial", 20, "normal"))