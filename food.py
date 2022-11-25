from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.shapesize(0.9)
        self.penup()
        self.food_move()

    def food_move(self):
        self.goto(random.randint(-270, 270),random.randint(-270, 270))
