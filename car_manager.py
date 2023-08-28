from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(1, 2)
        self.color(random.choice(COLORS))
        self.y = 0
        self.x = 0

        self.goto_start()

    def drive(self):
        self.goto(self.xcor() - MOVE_INCREMENT, self.y)

        if self.xcor() == -300:
            self.goto_start()

    def goto_start(self):
        self.y = random.randint(-250, 250)
        self.x = 300 + random.randrange(0, 600, 10)
        self.setpos(self.x, self.y)
