from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.hideturtle()
        self.goto(-260, 280)
        self.points = 0

    def increase_score(self):
        self.points += 1

    def update_score_board(self):
        self.clear()
        self.write(f"Score: {self.points}", align='center', font= ("Courier", 14, "normal"))
