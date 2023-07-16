from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        xval = random.randint(-270, 270)
        yval = random.randint(-270, 270)
        self.goto(xval, yval)
    def make_food(self):
        xval = random.randint(-270, 270)
        yval = random.randint(-270, 270)
        self.goto(xval, yval)
