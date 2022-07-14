from turtle import Turtle
tim = Turtle()
import random

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


colors = ["red", "black", "blue", "purple"]
directions = [0, 90, 180, 270]
speed = [0, 10, 6, 3, 1]

for _ in range(200):
    tim.pensize(20)
    tim.speed(0)
    tim.forward(30)
    tim.color(random.choice(colors))
    tim.setheading(random.choice(directions))
