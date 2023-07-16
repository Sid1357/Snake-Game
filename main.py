from turtle import Turtle, Screen
from snake import Snake
import time
from food import Food
from scorecard import Scorecard

my_screen = Screen()
my_screen.bgcolor("black")
my_screen.setup(height=600, width=600)
my_screen.title("My Snake Game")
my_screen.tracer(0)
my_screen.listen()

snake = Snake()
food = Food()
scorecard = Scorecard()

my_screen.onkey(snake.down, "Down")
my_screen.onkey(snake.up, "Up")
my_screen.onkey(snake.left, "Left")
my_screen.onkey(snake.right, "Right")



segments = []

is_on = True
while is_on:
    my_screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food)<15:
        food.make_food()
        scorecard.scoreincrement()
        snake.add_segment()
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        is_on = False
    for segment in snake.segments:
        if segment==snake.head:
            pass
        elif snake.head.distance(segment)<15:
            is_on = False
scorecard.game_over()









my_screen.exitonclick()
