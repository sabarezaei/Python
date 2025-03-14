from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT= 0


class Snake:

    def __init__(self):
        self.tts = []
        self.create_snake()
        self.head = self.tts[0]

    def create_snake(self):
        for position in (STARTING_POSITIONS):
            self.create_segmant(position)

    def create_segmant(self, pos):
        t = Turtle(shape="square")
        print(t)
        t.color("white")
        t.penup()
        t.goto(pos)
        self.tts.append(t)

    def extend(self):
        self.create_segmant(self.tts[-1].position())

    def move(self):
        for t in range(len(self.tts)-1, 0, -1):
            x = self.tts[t - 1].xcor()
            y = self.tts[t - 1].ycor()
            self.tts[t].goto(x, y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            self.move()

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            self.move()

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            self.move()

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            self.move()

    def detect_collision(self):
        ret = False
        for t in self.tts[1:]:
            if self.head.position() == t.position():
                ret = True
                continue

        return ret
