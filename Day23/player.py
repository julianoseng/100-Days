from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.speed(0)
        self.setheading(90)
        self.penup()
        self.goto(0, -70)

    def up(self):
        new_y = self.ycor() + 10
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 10
        self.goto(self.xcor(), new_y)

    def left(self):
        new_x = self.xcor() - 10
        self.goto(new_x, self.ycor())

    def right(self):
        new_x = self.xcor() + 10
        self.goto(new_x, self.ycor())

    def next_level(self):
        self.goto(0, -70)

    def start_over(self):
        self.goto(0, -70)
