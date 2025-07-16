from turtle import Turtle

class Score:

    def __init__(self):
        self.currentscore = 0
        self.score = Turtle("square")
        self.score.color("white")
        self.score.penup()
        self.score.hideturtle()
        self.score.goto(240, 280)
        self.score.write(f"Score: {self.currentscore}")

    def update(self):
        self.currentscore += 1
        self.score.reset()
        self.score.color("white")
        self.score.penup()
        self.score.hideturtle()
        self.score.goto(240, 280)
        self.score.write(f"Score: {self.currentscore}")