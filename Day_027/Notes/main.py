import tkinter
import turtle

window = tkinter.Tk()

window.title("My First GUI Program")

window.minsize(width=500, height=300)

# label
my_label = tkinter.Label(text="I Am a Label", font=("Ariel", 12, "bold"))
my_label.pack()

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