from turtle import Screen
from screen import Scoreboard
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong")
screen.listen()
screen.tracer(0)

scoreboard = Scoreboard()
ball = Ball()

# Draw scoreboard
scoreboard.draw_score()

player = Paddle(350, 0)
opponent = Paddle(-350, 0)

screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")


game_is_on = True
while game_is_on:
    time.sleep(.05)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 279 or ball.ycor() < -279:
        # Needs to bounce
        ball.bounce_y()

    # detect collision with paddles
    if ball.distance(player) < 50 and ball.xcor() > 320 or ball.distance(opponent) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect if player missed
    if ball.xcor() > 380:
        ball.reset_pos()
        scoreboard.opponent_add_score()

    # Detect if opponent missed
    if ball.xcor() < -380:
        ball.reset_pos()
        scoreboard.player_add_score()


screen.exitonclick()
