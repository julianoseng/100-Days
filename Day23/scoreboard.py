from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.level = 0

    def write_score(self):
        self.goto(-410, -70)
        self.write(f"Level = {self.level}", False, align="left", font=FONT)
        self.ht()

    def next_level(self):
        self.clear()
        self.level += 1
        self.goto(-410, -70)
        self.write(f"Level = {self.level}", False, align="left", font=FONT)
        self.ht()

    def start_over(self):
        self.clear()
        self.level = 0
        self.goto(-410, -70)
        self.write(f"Level = {self.level}", False, align="left", font=FONT)
        self.ht()
