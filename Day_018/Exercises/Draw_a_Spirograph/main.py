import turtle
from turtle import Turtle, exitonclick, Screen 
import random

tim = Turtle()
tim.shape("turtle")
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def draw_spirograph(gap):
    for _ in range(int(360 / gap)):
        tim.speed(0)
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + gap)

draw_spirograph(1)


screen = Screen()
screen = exitonclick()