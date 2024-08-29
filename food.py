from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.speed("fastest")

    def newwpos(self):
        x = random.randint(-180, 180)
        y = random.randint(-180, 180)
        self.goto(x, y)
