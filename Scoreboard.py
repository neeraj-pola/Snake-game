from turtle import Turtle
FONT = ("Arial", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = file.read()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.upgrade_score()

    def upgrade_score(self):
        self.clear()
        self.write(f"Score = {self.score}, High score = {self.high_score}", align="center", font=FONT)

    def increase_score(self):
        self.score += 1
        self.upgrade_score()

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.score}")

        self.score = 0
        self.upgrade_score()
