import tkinter
import turtle

window = tkinter.Tk()

window.title("My First GUI Program")

window.minsize(width=500, height=300)

# label
my_label = tkinter.Label(text="I Am a Label", font=("Ariel", 12, "bold"))
my_label.pack()

window.mainloop()

# timmy 

timmy = turtle.Turtle()
timmy.write()