from turtle import Turtle
import random

tim = Turtle()

tim.shape("turtle")
colours = ["red", "black", "blue", "purple"]

def shapes(num_sides):
    angle = 360 / num_sides
    for _ in range (num_sides):

        tim.forward(100)
        tim.right(angle)

for shape_side in range(3, 11):
    tim.color(random.choice(colours))
    shapes(shape_side)