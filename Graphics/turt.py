from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(height=500, width=400)
user_bet = screen.textinput(title="Make a bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []


for turtle_index in range(0, 6):
    tin = Turtle(shape="turtle")
    tin.color(colors[turtle_index])
    tin.penup()
    tin.goto(-150, y_positions[turtle_index])
    all_turtles.append(tin)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 150:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()