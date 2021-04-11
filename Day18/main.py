from turtle import Turtle, Screen
import random
tim = Turtle()
screen = Screen()
# tim.pensize(5)
tim.speed(0)
tim_turn = [0, 90, 180, 270]
screen.colormode(255)
color_list = [(199, 175, 117), (124, 36, 24), (168, 106, 57), (186, 158, 53), (6, 57, 83), (109, 67, 85),
              (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48)]
# turtle.dot(size=None, *color)
tim.penup()


def hirst_painting():
    tim.setheading(225)
    tim.forward(300)
    tim.setheading(0)
    for i in range(10):
        for i in range(10):
            tim.dot(15, random.choice(color_list))
            tim.forward(50)
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

hirst_painting()
tim.hideturtle()

# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     return color



# # Draws a spirograph
# def draw_spirograph(size_of_gap):
#     for i in range(int(360 / size_of_gap)):
#         tim.color(random_color())
#         tim.circle(100)
#         tim.setheading(tim.heading() + size_of_gap)
#
# draw_spirograph(5)

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