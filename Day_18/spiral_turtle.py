from turtle import Turtle, Screen, colormode
import random
from tk_colors import COLORS


def random_rgb():
    rgb = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return rgb


tut = Turtle()
colormode(255)
tut.speed('fastest')
for _ in range(1, 361):
    tut.pencolor(random_rgb())
    #tut.pencolor(random.choice(COLORS))
    tut.circle(100)
    tut.setheading(_)


sc = Screen()

sc.exitonclick()

