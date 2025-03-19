from turtle import Turtle

class Paddle (Turtle):

    def __init__(self, pos):
        super().__init__()
        self.penup()
        self.goto(pos)
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)


    def go_up (self):
        x, y = self.position()
        if y < 250:
            self.goto(x, y + 20)


    def go_down (self):
        x, y = self.position()
        if y > -250:
            self.goto(x, y - 20)

