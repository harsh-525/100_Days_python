from turtle import Turtle, Screen

tut = Turtle()
for _ in range(10):
    tut.forward(5)
    tut.pu()
    tut.forward(5)
    tut.pd()
sc = Screen()
sc.exitonclick()
