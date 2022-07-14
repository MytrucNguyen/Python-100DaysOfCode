from turtle import Turtle

tim = Turtle()

tim.shape("turtle")
tim.color("cyan", "black")

def dash():
    for _ in range(4):
        tim.forward(20)
        tim.penup()
        tim.forward(20)
        tim.pendown()
dash()