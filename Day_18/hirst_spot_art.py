import random
from turtle import Turtle, Screen, colormode
import colorgram

color_palette = colorgram. extract('hirst_art_sample_image.jpeg', 30)
rgb = []
colormode(255)
for _ in color_palette:
    rgb.append((_.rgb.r, _.rgb.g, _.rgb.b))
tut = Turtle()
tut.speed('fastest')
tut.hideturtle()
tut.setheading(225)
tut.pu()
tut.forward(400)
tut.setheading(0)


for x in range(10):
    for y in range(10):
        tut.color(random.choice(rgb))
        tut.dot(20)
        if y+1 != 10:
            tut.fd(50)
    if x % 2 == 0:
        tut.left(90)
        tut.fd(50)
        tut.left(90)
    else:
        tut.right(90)
        tut.fd(50)
        tut.right(90)

sc = Screen()
sc.exitonclick()



