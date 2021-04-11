from turtle import Turtle, Screen
import random
tim = Turtle()
screen = Screen()
# tim.pensize(5)
tim.speed(0)
tim_turn = [0, 90, 180, 270]
screen.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

angle = 0
for i in range(121):
    tim.circle(120)
    tim.setheading(angle)
    tim.pencolor(random_color())
    angle += 3


## Random path
# for i in range(200):
#     tim.forward(20)
#     tim.right(random.choice(tim_turn))
#     tim.pencolor(random_color())


## Dashed line
# for _ in range(10):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# # Draw a different shape each time
# def draw_shape(sides, degrees):
#     drawing = True
#     while drawing:
#         for _ in range(sides):
#             tim.forward(100)
#             tim.right(degrees)
#         sides += 1
#         degrees = 360 / sides
#         if sides > 11:
#             drawing = False
#
#
# draw_shape(3, 120)

screen.exitonclick()