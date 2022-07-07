from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.shape('square')
        self.pu()
        self.speed('fastest')
        self.color('white')
        self.setposition(x_pos, y_pos)
        self.shapesize(stretch_wid=5, stretch_len=1)

    def up(self):
        move = self.ycor() + 20
        if not move > 250:
            self.setposition(self.xcor(), move)
        else:
            self.setposition(self.xcor(), 250)

    def down(self):
        move = self.ycor() - 20
        if not move < -240:
            self.setposition(self.xcor(), move)
        else:
            self.setposition(self.xcor(), -240)
