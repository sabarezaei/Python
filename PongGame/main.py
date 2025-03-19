from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score_Board

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong")
screen.tracer(0)  # turn off the animation

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball=Ball()

l_score_board= Score_Board()
r_score_board= Score_Board()




screen. listen()

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# this part is for the screen tracer, it turns off the animation
game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    l_score_board.show("left")
    r_score_board.show("right")
    ball.move(l_paddle.ycor(),r_paddle.ycor())

    #Detect collision with top or bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with paddle
    if (ball.distance(r_paddle) <50 and ball.xcor()>300) or (ball.distance(l_paddle) <50 and ball.xcor()<-300) :
        ball.bounce_x()

    #Detect right or left miss
    if ball.xcor()> 400:
        time.sleep(1)
        ball.reset()
        l_score_board.left_counter+=1
    elif ball.xcor() < -400:
        time.sleep(1)
        ball.reset()
        r_score_board.right_counter += 1





screen.exitonclick()