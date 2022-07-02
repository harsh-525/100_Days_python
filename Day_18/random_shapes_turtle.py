from turtle import Turtle, Screen
import random
from tk_colors import COLORS


def shape(n):
    angle = 360 / n
    tut = Turtle()
    tut.pencolor(random.choice(COLORS))
    for _ in range(n):
        tut.forward(100)
        tut.right(angle)
        

for _ in range(3, 20):
    shape(_)
sc = Screen()
sc.exitonclick()
