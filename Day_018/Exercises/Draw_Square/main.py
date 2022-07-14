from turtle import Turtle

tim = Turtle()

tim.shape("turtle")
tim.color("cyan", "black")

def square():
    for _ in range(4):
        tim.forward(100)
        tim.right(90)

square()
