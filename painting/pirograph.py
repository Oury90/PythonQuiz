from turtle import Turtle, Screen, colormode
import random

tim = Turtle()
tim.speed("fastest")
colormode(255)
# tim.colormode(255)
# choice_value = random.randint(1, 255)
def color_mode():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    values_color = (r, g, b)
    return values_color


def draw_cercle(size):
    for _ in range(int(360 / size)):
        tim.pencolor(color_mode())
        tim.circle(100)
        position = tim.heading()
        tim.setheading(position + size)

draw_cercle(5)

screen = Screen()
screen.exitonclick()