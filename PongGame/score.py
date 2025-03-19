from turtle import Turtle


class Score_Board (Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_counter=0
        self.right_counter=0


    def show (self,side):
        self.clear()
        if side =="left":
            self.goto(-100,200)
            self.write(self.left_counter,align="center", font=("Arial", 70, "normal"))
        elif side =="right":
            self.goto(100,200)
            self.write(self.right_counter, align="center",font=("Arial", 70, "normal"))