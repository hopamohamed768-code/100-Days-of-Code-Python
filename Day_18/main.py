from turtle import Turtle, Screen
import random

color_list = [(213, 149, 88), (216, 80, 61), (45, 94, 144), (231, 218, 90), (147, 65, 92), (36, 19, 14), (39, 22, 28), (24, 28, 42), (213, 67, 86), (153, 71, 60), (116, 168, 197), (192, 138, 160), (38, 131, 92), (122, 179, 138), (75, 165, 94), (236, 221, 9), (229, 169, 182), (161, 176, 51), (51, 56, 102), (99, 44, 65), (18, 39, 27), (31, 167, 200), (105, 45, 40), (233, 173, 161), (165, 210, 192), (153, 207, 220)]
tim = Turtle()
screen = Screen()
screen.colormode(255)
for _ in range(10):
    for _ in range(10):
        dot_color = random.choice(color_list)
        tim.dot(20, dot_color)
        tim.penup()
        tim.fd(50)
        tim.pendown()
    tim.penup()
    tim.left(90)
    tim.fd(50)
    tim.left(90)
    tim.fd(500)
    tim.right(180)














screen.exitonclick()