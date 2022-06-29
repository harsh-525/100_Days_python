from turtle import Turtle, Screen

tut = Turtle()
tut.shape('turtle')
tut.color('red')
tut.forward(100)
s = Screen()
print(tut, s.canvheight)
s.exitonclick()
