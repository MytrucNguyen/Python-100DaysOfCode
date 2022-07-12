print("~~~~~~~~~~~~~~~~~ Day Sixteen ~~~~~~~~~~~~~~~\n")
print("~~~~~~~~~ Object Oriented Programming ~~~~~~~")

# Trying to model a real world object
# Things that they have = "attributes"; usually modeled with variables
# Thing that they can do = "methods"; modeled by functions
# Object = combining piece of data and some functionality 
# Classes = blueprint
print("~~~~~~~~~~~~~~~~~~~~ Turtle ~~~~~~~~~~~~~~~~~")
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# import turtle
# Leonardo = turtle.Turtle()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from turtle import Turtle, Screen

Leonardo = Turtle()
print(Leonardo)
Leonardo.shape("turtle")
Leonardo.color("cyan", "black")
Leonardo.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()