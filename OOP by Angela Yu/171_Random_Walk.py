from turtle import Turtle
import random

tim = Turtle()


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return "#{:02x}{:02x}{:02x}".format(r, g, b)

directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for i in range(200):
    color_hex = random_color()
    tim.color(color_hex)
    tim.forward(30)
    tim.setheading(random.choice(directions))
