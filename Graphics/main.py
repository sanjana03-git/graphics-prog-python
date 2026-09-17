# from turtle import Turtle, Screen

# tinny_the_turtle = Turtle()
# tinny_the_turtle.shape("turtle")
# tinny_the_turtle.color("coral")
# tinny_the_turtle.forward(100)
# tinny_the_turtle.left(90)
# tinny_the_turtle.forward(100)
# tinny_the_turtle.left(90)
# tinny_the_turtle.forward(100)
# tinny_the_turtle.left(90)
# tinny_the_turtle.forward(100)
# tinny_the_turtle.left(90)
# for _ in range(4):
#     tinny_the_turtle.forward(100)
#     tinny_the_turtle.left(90)


# for _ in range(15):
#     tinny_the_turtle.forward(10)
#     tinny_the_turtle.penup()
#     tinny_the_turtle.forward(10)
#     tinny_the_turtle.pendown()



# import turtle as t

# tin = t.Turtle()
# tin.shape("turtle")

# color_list = ["coral", "cyan", "magenta", "yellow", "blue", "green"]

num_sides = 5
# for _ in range(num_sides):
#     tin.forward(100)
    # tin.left(360 / num_sides)

# for shape_side_n in range(3, 11):
#     for _ in range(shape_side_n):
#         tin.color(color_list[shape_side_n - 3])
#         tin.forward(100)
#         tin.left(360 / shape_side_n)







# import turtle as t
# import random

# tin = t.Turtle()
# color_list = ["coral", "cyan", "magenta", "yellow", "blue", "green"]
# direction = [0, 90, 180, 270]
# tin.pensize(10)
# tin.speed("fastest")

# for _ in range(200):
#     tin.color(random.choice(color_list))
#     tin.forward(30)
#     tin.setheading(random.choice(direction))






# import turtle as t
# import random

# tin = t.Turtle()
# t.colormode(255)

# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return (r, g, b)

# direction = [0, 90, 180, 270]
# tin.pensize(10)
# tin.speed("fastest")
# tin.color(random_color())
# for _ in range(200):
#     tin.color(random_color())
#     tin.forward(30)
#     tin.setheading(random.choice(direction))

# my_screen = t.Screen()
# my_screen.exitonclick()



# spirograph
import turtle as t
import random

tin = t.Turtle()
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

tin.speed("fastest")
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tin.color(random_color())
        tin.circle(100)
        tin.setheading(tin.heading() + size_of_gap)

draw_spirograph(5) 

my_screen = t.Screen()
my_screen.exitonclick()