import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from car_manager import all_cars
from scoreboard import Scoreboard

player = Player()
screen = Screen()
screen.setup(width=900, height=900)
screen.tracer(0)
screen.listen()
scoreboard = Scoreboard()
scoreboard.write_score()
screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")
screen.onkey(player.right, "Right")
screen.onkey(player.left, "Left")
car_manager = CarManager()
car_manager.create_cars()


game_is_on = True


while game_is_on:

    if player.ycor() >= 380:
        scoreboard.next_level()
        player.next_level()

    for car in all_cars:
        if player.distance(car) < 40:
            scoreboard.start_over()
            player.start_over()

    time.sleep(0.05)
    car_manager.move_around(game_is_on)
    screen.update()


screen.exitonclick()
