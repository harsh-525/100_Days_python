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


def food():
    global snack
    snack = Turtle(shape='circle')
    snack.pu()
    snack.shapesize(stretch_len=.5, stretch_wid=.5)
    snack.color('blue')
    snack.speed('fastest')
    snack.setposition(random.randint(-280, 200), random.randint(-280, 200))
    return snack.xcor()


def show_score(count):
    score.reset()
    score.hideturtle()
    score.pu()
    score.hideturtle()
    score.setposition(0, 280)
    score.write(arg=f"Score: {count}", move=True, align='center', font=('Courier', 15, 'normal'))


def eat():
    global count
    if tuts[0].distance(snack) < 15:
        count += 1
        snack.hideturtle()
        show_score(count) #update score_board
        food() #generate random food
        return True


def snake_growth():
    new_segment = Turtle(shape='square')
    new_segment.pu()
    new_segment.setposition(tuts[-1].xcor() - 20, tuts[-1].ycor())
    tuts.append(new_segment)


def game():
    tut1 = Turtle(shape='square')
    tut1.pu()
    tut2 = Turtle(shape='square')
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
        if eat():
            snake_growth()
        if tuts[0].xcor() > 280 or tuts[0].xcor() < -280 or tuts[0].ycor() > 280 or tuts[0].ycor() < -280:
            print("WALL HIT")
            return True
        for x in tuts[1:]:
            if tuts[0].distance(x) < 5:
                print("HIT BODY")
                return True


food()
global score
score = Turtle()
score.hideturtle()

global count
count = 0
show_score(count)


sc = Screen()
sc.bgcolor('gray')
sc.setup(width=600, height=600)
sc.title('-SNAKE GAME-')
sc.listen()


sc.tracer(0)
count = 0
if game():
    score.goto(0,0)
    score.write("GAME OVER", align="CENTER", font=('Courier', 25, 'normal'))


sc.exitonclick()
