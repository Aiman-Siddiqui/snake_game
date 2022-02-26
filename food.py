from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)

COLOR_LIST = [(238, 223, 204), (118, 238, 198), (227, 207, 87), (255, 97, 3), (61, 89, 171), (255, 114, 86), (255, 248,
                                                                                                              220),
              (238, 232, 205), (220, 20, 60), (0, 205, 205), (0, 139, 139), (255, 185, 15), (0, 100, 0), (100, 0, 0),
              (0, 0, 100), (154, 50, 205), (255, 20, 147), (255, 48, 48), (255, 125, 64), (255, 110, 180), (173, 255,
                                                                                                            47),
              (178, 223, 238), (255, 236, 139), (32, 178, 170), (199, 21, 133), (85, 26, 139), (145, 44, 238),
              (255, 255, 0), (128, 128, 105)]

SHAPES = ["circle", "square", "turtle"]


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.7, 0.7)
        self.color(random.choice(COLOR_LIST))
        self.speed(0)
        self.place_food()

    def place_food(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 260)
        self.color(random.choice(COLOR_LIST))
        self.shape(random.choice(SHAPES))
        self.goto(random_x, random_y)
