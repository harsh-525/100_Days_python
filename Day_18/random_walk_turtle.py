from turtle import Turtle, Screen
from tk_colors import COLORS
import random

directions = [0, 90, 180, 270]
tut = Turtle()
tut.width(10)
tut.speed('fastest')
for _ in range(100):
    tut.pencolor(random.choice(COLORS))
    tut.setheading(random.choice(directions))
    tut.forward(20)
sc = Screen()
sc.exitonclick()
