import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Screen set up
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Player obj
player = Player()

# Cars
cars = []
num_cars = random.randint(20, 30)
for _ in range(num_cars):
    car = CarManager()
    cars.append(car)

# Event-Listener set up
screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    for car in cars:
        car.drive()
