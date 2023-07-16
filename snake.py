from turtle import Turtle
GOTO_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
RIGHT = 0
LEFT = 180
DOWN = 270


class Snake:
    def __init__(self):
        self.segments = []
        for i in range(3):
            tim = Turtle()
            tim.shape("square")
            tim.color("white")
            tim.penup()
            tim.speed("normal")
            tim.goto(GOTO_POSITIONS[i])
            self.segments.append(tim)
            self.head = self.segments[0]
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            newxcor = self.segments[seg_num - 1].xcor()
            newycor = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(newxcor, newycor)
        self.segments[0].forward(20)
    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)
    def add_segment(self):
        tim = Turtle()
        tim.shape("square")
        tim.color("white")
        tim.penup()
        tim.speed("normal")
        xcor = self.segments[len(self.segments)-1].xcor()-20
        ycor = self.segments[len(self.segments)-1].ycor()-20
        self.segments.append(tim)
        tim.goto(xcor, ycor)


