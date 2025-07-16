import time
from turtle import *
from snake import Snake
from food import Food
from score import Score

screen = Screen()

screen.setup(600, 600)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()

game_on = True

screen.listen()

screen.onkey(snake.move_up, "w")
screen.onkey(snake.move_down, "s")
screen.onkey(snake.move_left, "a")
screen.onkey(snake.move_right, "d")

food = Food()

currentscore = 0

scoreboard = Score()

while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.add()
        scoreboard.update()

    if snake.head.xcor() >= 300 or snake.head.xcor() <= -300 or snake.head.ycor() >= 300 or snake.head.ycor() <= -300:
        game_on = False

    for piece in snake.pieces:
        if piece == snake.head:
            pass
        elif snake.head.distance(piece) < 10:
            game_on = False

screen.reset()
t = Turtle()
t.color("white")
t.write("YOU LOSE", align="center", font=("Courier", 30, "bold"))

screen.exitonclick()