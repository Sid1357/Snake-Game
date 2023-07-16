from turtle import Turtle

class Scorecard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(-60, 230)
        self.color("white")
        self.pensize(40)
        self.shapesize(0.1)
        self.write("Score: 0", font=("Arial", 20, "normal"))
    def scoreincrement(self):
        self.clear()
        self.score+=1
        self.write(f"Score: {self.score}", font=("Arial", 20, "normal"))
    def game_over(self):
        self.clear()
        self.goto(-100, 230)
        self.write(f"Your final score was {self.score}", font=("Arial", 20, "normal"))
