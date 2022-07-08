from turtle import Turtle, Screen
from Day_18 import tk_colors
from player import Player
from score import Score
from cars import Cars
import time


# TODO 1: create the screen
sc = Screen()
sc.title("Turtle Crossing")
sc.setup(width=600, height=600)
sc.bgcolor('snow')
sc.tracer(0)  # turn off animation

# TODO 2: make the player
tut = Player()
sc.update()

# TODO 3: move the player
game_on = True
sc.listen()
sc.onkeypress(tut.move, "Up")

# TODO 5: create the score board
points = Score()
points.update_score_board()

# TODO 6: Create cars
vehs = []
for _ in range(30):
    vehs.append(Cars())


while game_on:
    sc.update()
    time.sleep(0.05)

    for i in range(len(vehs)):
        vehs[i].move()

    # TODO 4 detect top line, reset to starting line and increase score
    if tut.ycor() == 280:
        tut.reset_pos()
        points.increase_score()
        points.update_score_board()

    # TODO 7: Detecting collision with a car
    # if tut.distance(vehicle) <= 20:
    #     print(tut.distance(vehicle))
    #     print('collision')
    #     game_on = False

sc.exitonclick()
