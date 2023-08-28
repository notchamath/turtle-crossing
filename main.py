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
screen.title("Turtle Crossing")

# Scoreboard
score = Scoreboard()

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
    time.sleep(score.game_speed)
    screen.update()

    for car in cars:
        # Move car
        car.drive()

        # If car collision with turtle, game over
        if car.distance(player) < 25:
            game_is_on = False
            score.game_over()

    # If Turtle reaches finish line, increase level
    if player.ycor() > score.finish_line:
        player.player_reset()
        score.level_up()

screen.exitonclick()
