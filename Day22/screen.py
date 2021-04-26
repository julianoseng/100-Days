from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.player_score = 0
        self.opponent_score = 0
        self.speed(0)
        self.color("white")
        self.penup()

    def draw_score(self):
        self.clear()
        self.goto(40, 230)
        self.write(f"{self.player_score}", False, align="center", font=("Arial", 60, "normal"))
        self.goto(-40, 230)
        self.write(f"{self.opponent_score}", False, align="center", font=("Arial", 60, "normal"))
        self.ht()

    def player_add_score(self):
        self.player_score += 1
        self.draw_score()

    def opponent_add_score(self):
        self.opponent_score += 1
        self.draw_score()
