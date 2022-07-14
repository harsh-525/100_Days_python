import turtle
from turtle import Turtle, Screen
import pandas as pd
import time


sc = Screen()
sc.title('U.S. States Game')
img = 'blank_states_img.gif'
sc.addshape(img)
turtle.shape(img)
sc.tracer(0)  # turn off animation

guessed_states = []
data = pd.read_csv('50_states.csv')

states = data.state.to_list()
for i in range(len(states)):
    states[i] = states[i].lower()

while len(guessed_states) <= 50:
    answer = sc.textinput(title=f'{len(guessed_states)}/50 Guess the state name',
                          prompt="what's the US state name").lower()
    if answer in states and answer not in guessed_states:
        guessed_states.append(answer)
        sc.update()
        time.sleep(0.1)
        # answer = sc.textinput(title=f'{point}/50 Guess the state name', prompt="what's the US state name")
        tut = Turtle()
        tut.hideturtle()
        tut.pu()
        x_cor = int(data[data.state.str.lower() == answer.lower()].x)
        y_cor = int(data[data.state.str.lower() == answer.lower()].y)
        tut.goto(x_cor, y_cor)
        tut.pd()
        tut.write(answer.lower())
    elif answer in guessed_states:
        answer = sc.textinput(title=f'{len(guessed_states)}/50 Guess the state name',
                              prompt=f"{answer.capitalize()} Already Guessed\nwhat's the new US state name")
        sc.update()
        time.sleep(0.1)
    elif answer == 'exit':
        break

missed = {'state': [], 'x': [], 'y': []}
for _ in states:
    if _ not in guessed_states:
        missed['state'].append(_.title())
        missed['x'].append(int(data[data.state == _.title()].x))
        missed['y'].append(int(data[data.state == _.title()].y))

pd.DataFrame(missed).to_csv('missed_states.csv')

sc.exitonclick()
