import tkinter
import turtle
from tkinter import *

window = tkinter.Tk()

window.title("My First GUI Program")

window.minsize(width=500, height=300)

# label
my_label = tkinter.Label(text="I Am a Label", font=("Ariel", 12, "bold"))
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="Next Text 2")



# Button
def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)

button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()

# Entry 
input = Entry(width=10)
input.pack()


window.mainloop()

# tim

tim = turtle.Turtle()
tim.write("Some Text", font=("Times New Roman", 30, "bold"))

# Unlimited Arguments
def add(*args):
    total = 0
    for num in args:
        total += num
    return total

print(add(3, 5, 6))

# *kwargs
def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)

    # print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["mutiply"]
    print('n', n)

calculate(2, add=3, mutiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")

my_car = Car(make="Nissan")
print(my_car.model)
