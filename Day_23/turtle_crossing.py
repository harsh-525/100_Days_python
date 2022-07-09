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
sc.bgcolor('gray')
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
for _ in range(15):
    vehs.append(Cars())

cars_speed = 0.1

nearest = 500
while game_on:
    #  print(f"cars_speed: {cars_speed}")
    sc.update()
    time.sleep(cars_speed)
    y_cor = {}
    for i in range(len(vehs)):  # moving cars
        vehs[i].move()

    # TODO 4 detect top line, reset to starting line and increase score
    if tut.ycor() == 280:
        tut.reset_pos()
        cars_speed -= 0.02
        points.increase_score()
        points.update_score_board()

    # TODO 7: Detecting collision with a car
    for _ in vehs:
        if tut.distance(_) <= 25:
            print(tut.distance(_), tut.position(), _.position())
            print('collision')
            points.game_over()
            game_on = False

sc.exitonclick()
