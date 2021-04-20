import sys
import turtle
import math


def draw_circle(radius):
    turtle.color('green')
    turtle.speed("fast")
    counter_y_crossed = False
    x_sign = 1.0
    while not counter_y_crossed:
        turtle.forward(2 * math.pi * radius / 360.0)
        turtle.right(1.0)
        new_x = math.copysign(1, turtle.xcor())   
        if (new_x != x_sign):
            counter_y_crossed = True
        x_sign = new_x
    turtle.done()
    turtle.circle()


if __name__ == "__main__":
    draw_circle(int(sys.argv[1]))