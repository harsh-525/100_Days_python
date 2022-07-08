from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.pu()
        self.left(90)
        self.goto(0, -280)

    def move(self):
        self.fd(10)

    def reset_pos(self):
        self.goto(0, -280)
