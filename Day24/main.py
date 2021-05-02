from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# # mode = w (write) (clears everything already within the file)
# # mode = r (read only) (cant make any changes)
# # mode = a (append) (you can add things without clearing the file)
# with open("high_score_save.txt", mode="w") as file:
#     # contents = file.read()
#     # prints contents)
#     # print(contents)
#     # writes a new line of text to the contents
#     file.write("New Text.")

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        scoreboard.add_score()
        snake.extend()
        food.refresh()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        snake.reset_snake()
        scoreboard.reset()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            snake.reset_snake()
            scoreboard.reset()
    # if head collides with any segment in the tail:
        # trigger game over


screen.exitonclick()
