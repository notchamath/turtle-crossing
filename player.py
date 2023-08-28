from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.player_reset()

    def move(self):
        self.goto(0, self.ycor() + MOVE_DISTANCE)

    def player_reset(self):
        self.goto(STARTING_POSITION)
