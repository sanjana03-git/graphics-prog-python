from turtle import Screen, Turtle

tin = Turtle()
screen = Screen()

def move_forward():
    tin.forward(10)

def move_backward():
    tin.backward(10)

def turn_left():
    new_heading = tin.heading() + 10
    tin.setheading(new_heading)

def turn_right():
    new_heading = tin.heading() - 10
    tin.setheading(new_heading)

def clear_screen():
    tin.clear()
    tin.penup()
    tin.home()
    tin.pendown()

screen.listen()

screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear_screen, "c")
# screen.exitonclick() 
# turn_left()
screen.mainloop()