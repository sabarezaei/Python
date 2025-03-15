from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

counter = 0
snake = Snake()
food = Food()
score = Score()
game_is_on = True

while game_is_on:
    screen.listen()
    screen.update()
    time.sleep(0.1)
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.left, "Left")
    if snake.head.distance(food) < 20:
        food.refresh()
        score.increase_score()
        snake.extend()

    if (snake.head.ycor() <= -300 or snake.head.ycor() >= 300) or (snake.head.xcor() <= -300 or snake.head.xcor() >= 300):
        game_is_on = False
        score.game_over()

    if snake.detect_collision():
        game_is_on = False
        score.game_over()



screen.exitonclick()