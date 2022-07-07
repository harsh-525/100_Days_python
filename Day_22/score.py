from turtle import Turtle
L_ALIGNMENT = "left"
R_ALIGNMENT = "right"
FONT = ("Courier", 14, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.color("white")
        self.goto(0, 280)
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0

    def increase_score(self, player):
        if player == 'left':
            self.left_score += 1
        else:
            self.right_score += 1

    def update_score(self):
        self.write(f"Score: {self.left_score}\t", align=R_ALIGNMENT, font=FONT)
        self.write(f"\tScore: {self.right_score}", align=L_ALIGNMENT, font=FONT)

