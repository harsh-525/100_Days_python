from turtle import Turtle
from Day_18 import tk_colors
import random


class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.pu()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.goto(random.randint(-300, 300), random.randint(-240, 270))
        self.color(random.choice(tk_colors.COLORS))
        self.left(180)

    def move(self):
        self.fd(10)
        if self.xcor() < -300:
            self.goto(random.randint(320, 450), random.randint(-240, 275))
