from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time


# TODO 1: create a screen
sc = Screen()
sc.title("Pong")
sc.setup(width=800, height=600)
sc.bgcolor('black')
sc.tracer(0)  # turn off animation

line1 = Turtle()
line2 = Turtle()
line1.color('white')
line2.color('white')
line1.left(90)
line1.pensize(width=5)
line2.pensize(width=5)
line2.right(90)
for _ in range(20):
    line1.fd(10)
    line2.fd(10)
    line1.pu()
    line2.pu()
    line1.fd(10)
    line2.fd(10)
    line1.pd()
    line2.pd()

# TODO 2: create paddles and move them
# paddles created
player_a = Paddle(-390, 0)
player_b = Paddle(380, 0)
sc.update()  # update the screen to show animations

# moving paddles
sc.listen()
sc.onkey(player_b.up, "Up")
sc.onkey(player_b.down, "Down")
sc.onkey(player_a.up, "w")
sc.onkey(player_a.down, "s")

# TODO 3: create a ball and move
b = Ball()

score = Score()
score.update_score()

game = True
while game:
    sc.update()
    b.move()
    time.sleep(.1)  # slow down the ball speed because of while loop
    # TODO 4: top and bottom wall collision bounce
    if b.ycor() >= 280 or b.ycor() <= -280:  # top and bottom wall collisions
        b.bounce_y()

    # TODO 5: collision with paddle and bounce
    if (b.distance(player_b) < 50 and b.xcor() > 350) or (b.distance(player_a) < 50 and b.xcor() < -360):
        b.bounce_x()

    # TODO 6: ball misses the paddle and go out of bounds
    if b.xcor() > 370:  # Right player misses
        b.reset()
        score.increase_score('left')
        score.clear()
        score.update_score()

    if b.xcor() < -360:  # left player misses
        b.reset()
        score.increase_score('right')
        score.clear()
        score.update_score()

sc.exitonclick()
