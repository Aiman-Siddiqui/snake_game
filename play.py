from turtle import Turtle

class Play(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 0)
        self.color("white")
        self.write("Press spacebar to start the game")


