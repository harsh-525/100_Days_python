from turtle import Turtle, Screen
import random


def race_started(players, bet):
    while True:
        for _ in players:
            rand_dist = random.randint(1, 10)
            _.fd(rand_dist)
            # print(_.pencolor(), _.xcor())
            if _.xcor() >= 214:
                print(f'{_.pencolor()} is the WINNER')
                if _.pencolor() == bet:
                    return True
                else:
                    return False


sc = Screen()
sc.listen()
sc.bgcolor('gray')
sc.setup(width=500, height=400)
user_bet = sc.textinput(title="Make your bet", prompt="Which color turtle wins the race?")
vibgyor = ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']
referee = Turtle()
referee.speed('fastest')
tuts = []
y = -100 # starting pos of players

# draw the lanes
referee.pu()
referee.goto(x=-240, y=y - 15)
referee.pd()
referee.fd(490)

for i in range(len(vibgyor)):
    a = Turtle(shape='turtle')
    a.color(vibgyor[i])
    tuts.append(a)
    tuts[i].pu()
    referee.pu()
    referee.goto(x=-240, y=y + 15)
    referee.pd()
    referee.fd(490)
    tuts[i].goto(x=-230, y=y)
    y += 30

# Draw finish line
referee.pu()
referee.goto(x=230, y=y + 30)
referee.right(90)
referee.pd()
referee.fd(290)

if race_started(tuts, user_bet):
    print('YAY! You won the bet')
else:
    print('You lost the bet')
sc.exitonclick()
