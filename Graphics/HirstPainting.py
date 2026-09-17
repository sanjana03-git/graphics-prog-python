# import colorgram

# rgb_colors = []
# colors = colorgram.extract('Graphics/image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

from itertools import count
import turtle as t
import random

t.colormode(255)
tin = t.Turtle()
tin.speed("fastest")
tin.penup()
tin.hideturtle()
number_of_dots = 100
color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35)]

tin.setheading(225)
tin.forward(300)
tin.setheading(0)

for dot_count in range(1, number_of_dots + 1):
    tin.dot(20, random.choice(color_list))
    tin.forward(50)


    if dot_count % 10 == 0:
        tin.setheading(90)
        tin.forward(50)
        tin.setheading(180)
        tin.forward(500)
        tin.setheading(0)


screen = t.Screen()
screen.exitonclick()