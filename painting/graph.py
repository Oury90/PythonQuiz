from turtle import Turtle, Screen
import random

colors = [
    "red", "blue", "green", "yellow", "purple", "orange", "pink", "brown",
    "black", "white", "gray", "cyan", "magenta", "lime", "gold", "navy",
    "teal", "maroon", "olive", "violet", "indigo"
]

direction_angle = [0, 90, 180, 270]
tim = Turtle()

number = 1

while number > 0:
    tim.pensize(5)
    tim.forward(20)
    tim.color(random.choice(colors))
    tim.right(random.choice(direction_angle))












screen = Screen()
screen.exitonclick()