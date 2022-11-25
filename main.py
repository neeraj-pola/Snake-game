from turtle import Turtle,Screen
from snake import Snake
from food import Food
from Scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600,height=600)
screen.tracer(0)

score = Scoreboard()
snake = Snake()
food = Food()


screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.right, key="Right")
screen.onkey(fun=snake.left, key="Left")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    # detect collisions:
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.reset()
        snake.reset()
    # collision with food:
    if snake.head.distance(food) < 20 :
        snake.extend_snake()
        food.food_move()
        score.increase_score()

    # collisoin with snake tail:
    for seg in snake.segment[1:]:
        if snake.head.distance(seg) < 10:
            score.reset()
            snake.reset()
















screen.exitonclick()