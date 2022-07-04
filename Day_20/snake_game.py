from turtle import Turtle, Screen
import random, time


def turn_left(tut):
    return tut.left(90)


def turn_right(tut):
    return tut.right(90)


def game():
    tut1 = Turtle(shape='square')
    tut2 = Turtle(shape='square')
    tut2.color('red')
    tut2.pu()
    tut2.setposition(tut1.xcor() - 20, tut1.ycor())
    tuts = [tut1, tut2]
    sc.update()
    sc.listen()
    i=0
    while i<10:
        sc.update()
        time.sleep(.1)
        for _ in range(len(tuts)-1, 0, -1):
            tuts[_].pu()
            tuts[_].setposition(tuts[_+-1].xcor(), tuts[_-1].ycor())
        tuts[0].fd(20)
        sc.onkeypress(key="Up", fun=turn_left)
        sc.onkeypress(key='Right', fun=turn_right)
        i+=1




sc = Screen()
sc.bgcolor('gray')
sc.setup(width=600, height=600)
sc.title('-SNAKE GAME-')

sc.tracer(0)
game()

sc.exitonclick()
