import turtle
from turtle import Turtle,Screen
import random


turtle.colormode(255)
timmy = Turtle(shape="turtle")
timmy.color("pink")
timmy.pensize(8)
timmy.speed("fastest")

angles=[0,90,180,270]
for _ in range (100):
    rotation=random.choice(angles)
    r=random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    timmy.right(rotation)
    timmy.forward(30)
    timmy.pencolor((r , g , b))





"""for _ in range (4):
    timmy.forward(100)
    timmy.right(90)

for i in range (4,9):
    rotate=360/i
    for _ in range (i):
        timmy.forward(100)
        timmy.right(rotate)"""


screen = Screen()
screen.exitonclick()