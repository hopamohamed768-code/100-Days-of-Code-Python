from turtle import Screen
import time
from food import Food
from snake import Snake
from scoreboard import Score

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

my_snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(my_snake.up,"Up")
screen.onkey(my_snake.down,"Down")
screen.onkey(my_snake.left,"Left")
screen.onkey(my_snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    my_snake.move()

    # Detect collision with food.
    if my_snake.segments[0].distance(food) < 15:
        food.refresh()
        my_snake.extend()
        score.increase_score()

    # Detect collision with wall.
    if my_snake.segments[0].xcor() > 280 or my_snake.segments[0].xcor() < -280 or my_snake.segments[0].ycor() > 280 or my_snake.segments[0].ycor() < -280:
        score.reset()
        my_snake.reset()
    # Detect collision with tail.
    for segment in my_snake.segments[1:]:
        if my_snake.segments[0].distance(segment) < 10:
            score.reset()
            my_snake.reset()





screen.exitonclick()
