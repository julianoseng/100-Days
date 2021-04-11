from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
y_positions = [-80, -40, 0, 40, 80]
all_turtles = []


for turtle_index in range(0, 5):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner.")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)



screen.exitonclick()



# def move_forwards():
#
#     tim.forward(10)
#
#
# def move_backwards():
#     tim.back(10)
#
#
# def counter_clockwise():
#     tim.left(5)
#
#
# def clock_wise():
#     tim.right(5)
#
#
# def clear_screen():
#     tim.reset()
#
#
# def etch_a_sketch():
#
#     screen.listen()
#     screen.onkey(key="w", fun=move_forwards)
#     screen.onkey(key="s", fun=move_backwards)
#     screen.onkey(key="a", fun=counter_clockwise)
#     screen.onkey(key="d", fun=clock_wise)
#     screen.onkey(key="c", fun=clear_screen)
#     screen.exitonclick()
#
# etch_a_sketch()