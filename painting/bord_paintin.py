from turtle import Turtle, Screen, colormode
import random

list_colors = [(59, 99, 144), (209, 125, 172), (225, 148, 88), (119, 158, 199), (137, 69, 119), (210, 83, 147), (54, 123, 71), (133, 100, 54), (138, 23, 69), (39, 53, 114), (98, 115, 188), (32, 37, 81), (223, 209, 100), (178, 150, 50), (242, 155, 206), (174, 217, 247), (127, 171, 154), (170, 173, 242), (28, 61, 38), (89, 150, 116), (61, 48, 19), (243, 188, 242), (138, 28, 20), (235, 90, 66), (82, 21, 50), (33, 85, 45), (84, 144, 161), (79, 76, 28), (134, 213, 232), (135, 221, 209), (238, 210, 156), (171, 238, 230), (22, 78, 97), (237, 163, 156), (209, 206, 39)]

bord = Turtle()
colormode(255)

bord.speed("fastest")
bord.setheading(225)
bord.hideturtle()
bord.penup()
bord.forward(400)
bord.setheading(0)

number_tur = 600

for i in range(1, number_tur +1):
    bord.dot(10, random.choice(list_colors))
    bord.forward(20)

    if i % 30 == 0:
        bord.left(90)
        bord.forward(30)
        bord.left(90)
        bord.forward(600)
        bord.setheading(0)








screen = Screen()
screen.exitonclick()