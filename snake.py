from turtle import Turtle

class Snake:
    def __init__(self):
        self.pieces = []
        self.create()
        self.head = self.pieces[0]
        self.move_lock = False

    def create(self):
        starting = 0
        for i in range(0, 3):
            turt = Turtle(shape="square")
            turt.color("white")
            turt.penup()
            turt.goto(starting, 0)
            starting -= 20
            self.pieces.append(turt)

    def add(self):
        new = Turtle(shape="square")
        new.hideturtle()
        new.color("white")
        new.penup()
        self.pieces.append(new)

    def move(self):
        for i in range(len(self.pieces) - 1, 0, -1):
            self.pieces[i].showturtle()
            newx = self.pieces[i - 1].xcor()
            newy = self.pieces[i - 1].ycor()
            self.pieces[i].goto(newx, newy)
        self.pieces[0].forward(20)
        self.move_lock = False

    def move_up(self):
        if not self.move_lock and self.pieces[0].heading() != 270.0:
            self.pieces[0].setheading(90)
            self.move_lock = True


    def move_left(self):
        if not self.move_lock and self.pieces[0].heading() != 0.0:
            self.pieces[0].setheading(180)
            self.move_lock = True

    def move_down(self):
        if not self.move_lock and  self.pieces[0].heading() != 90.0:
            self.pieces[0].setheading(270)
            self.move_lock = True

    def move_right(self):
        if not self.move_lock and  self.pieces[0].heading() != 180:
            self.pieces[0].setheading(0)
            self.move_lock = True


