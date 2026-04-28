from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width = 500, height = 400)

is_race_on = False
bet = screen.textinput(title = 'MAke a bet', prompt= "which turtle will win the game?")

colors = ['red', 'blue','yellow', 'purple', 'green', 'orange']
turtle_list = []

for i,c in enumerate(colors) :
    t = Turtle(shape= "turtle")
    t.color(c)
    t.penup()
    t.speed("fastest")
    t.goto(x = -230, y = -180 +(i+1)*50)
    turtle_list.append(t)

def move_forward (t):
   t.forward(random.randint(1,10))
   

if bet:
    is_race_on = True


while is_race_on:
    for tur in turtle_list:
        if tur.xcor()> 230:
            print (f' {tur.pencolor()} turtle won the race' )
            is_race_on = False
        
        move_forward(tur)
    
    
    
    
    
    
    
screen.exitonclick()