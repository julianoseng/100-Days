from turtle import Turtle
UP = 90
DOWN = 270


class Paddle(Turtle):

    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.setposition(x_pos, y_pos)
        self.penup()
        self.speed(0)
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
