from turtle import Turtle, Screen
import random

timmy = Turtle()

colors = ["red", "green", "blue", "yellow"]

# number_angle = 5

def draw_shap(number_angle):
    for _ in range(number_angle):
        angle = 360 / number_angle
        timmy.forward(100)
        timmy.right(angle)


for shap_number in range(3, 11):
    draw_shap(shap_number)
    timmy.color(random.choice(colors))














screen = Screen()
screen.exitonclick()