import turtle
from turtle import Turtle, Screen
from random import randint, uniform, choice

def random_color():
    color_in_list = []
    for _ in range(3):
        color_in_list.append(randint(0, 255))
    return tuple(color_in_list)

timmy = Turtle()
tom = Turtle()
turtle.colormode(255)
timmy.shape("turtle")

x = 0
timmy.speed(100)
for _ in range(36):
    timmy.color(random_color())
    timmy.circle(100)
    timmy.setheading(x)
    x += 10


tup_color = random_color()
# shapes = [120, 90, 72, 60, 51.43, 45, 40, 36]
# angle = 3


# for shape in shapes:
#     for _ in range(angle):
#         timmy.forward(100)
#         timmy.right(shape)
#     angle += 1
#     timmy.pencolor(tup_color)

# TODO: Move 10 paces, pick turning angle
# def left_or_right():
#     direction = ["left", "right"]
#     facing = choice(direction)
#     if facing == "left":
#         return timmy.left(round(uniform(0, 360), 2))
#     else:
#         return timmy.right(round(uniform(0, 360), 2))
#
#
# walking = True
# timmy.pensize(10)
# timmy.speed(9)
#
# while walking:
#     for _ in range(100):
#         tup_color = random_color()
#         timmy.color(tup_color)
#         timmy.forward(randint(0, 100))
#         left_or_right()
#     walking = False

screen = Screen()
screen.exitonclick()
