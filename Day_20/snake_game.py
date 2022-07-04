from turtle import Turtle, Screen
import random, time


def turn_up():
    return tuts[0].setheading(90)


def turn_down():
    return tuts[0].setheading(270)


def turn_left():
    return tuts[0].setheading(180)


def turn_right():
    return tuts[0].setheading(0)


def game():
    tut1 = Turtle(shape='square')
    tut2 = Turtle(shape='square')
    tut2.color('red')
    tut2.pu()
    tut2.setposition(tut1.xcor() - 20, tut1.ycor())
    global tuts
    tuts = [tut1, tut2]
    sc.update()

    while True:
        sc.update()
        time.sleep(.1)
        for _ in range(len(tuts)-1, 0, -1):
            tuts[_].pu()
            tuts[_].setposition(tuts[_+-1].xcor(), tuts[_-1].ycor())
        tuts[0].fd(20)
        sc.onkeypress(key="Up", fun=turn_up)
        sc.onkeypress(key='Right', fun=turn_right)
        sc.onkeypress(key="Left", fun=turn_left)
        sc.onkeypress(key='Down', fun=turn_down)






sc = Screen()
sc.bgcolor('gray')
sc.setup(width=600, height=600)
sc.title('-SNAKE GAME-')
sc.listen()


sc.tracer(0)
game()

sc.exitonclick()
