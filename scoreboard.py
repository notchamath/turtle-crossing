from turtle import Turtle

FONT = ("Courier", 20, "normal")
FINISH_LINE = 280


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.setpos(-260, 260)
        self.game_speed = 0.1
        self.finish_line = FINISH_LINE

        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align="center", font=FONT)

    def level_up(self):
        self.level += 1
        self.game_speed *= 0.5
        self.write_score()
