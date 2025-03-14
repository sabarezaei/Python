from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.write(f"Score : {self.count}", False, align="center", font=("Arial", 15, "normal"))

    def increase_score(self):
        self.count +=1
        self.clear()
        self.write(f"Score : {self.count}", False, align="center", font=("Arial", 15, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", False, align="center", font=("Arial", 20, "normal"))

