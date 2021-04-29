import random
import time
from turtle import Turtle
from scoreboard import Scoreboard
from player import Player

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
all_cars = []


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(1.0, 3.0)
        self.setheading(180)
        all_cars.append(self)

    def create_cars(self):
        for color in range(0, len(COLORS)):
            new_car = CarManager()
            new_car.color(COLORS[color])
            new_car.goto(random.randint(-430, 430), random.randint(20, 430))

    def move_around(self, game_is_on):
        if game_is_on:
            for car in all_cars:
                car.forward(STARTING_MOVE_DISTANCE)
                if car.xcor() < -445:
                    car.goto(random.randint(-430, 430), random.randint(20, 430))
