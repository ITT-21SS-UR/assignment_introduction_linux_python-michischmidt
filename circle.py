import sys
import turtle
import math


def draw_circle(radius):
    turtle.color('green')
    turtle.speed("fastest")
    counter_y_crossed = 0
    x_sign = 1.0
    while counter_y_crossed <= 1:
        turtle.forward(2 * math.pi * radius / 360.0)
        turtle.right(1.0)
        new_x = math.copysign(1, turtle.xcor())   
        if (new_x != x_sign):
            counter_y_crossed += 1
        x_sign = new_x
    turtle.done()


def draw_good_circle(radius):
    turtle.color('green')
    turtle.dot(radius + 1)
    turtle.color('white')
    turtle.dot(radius - 1)
    turtle.done()


if __name__ == "__main__":
    print("Choose drawing bad circle 1 or good circle 2:")
    input = int(sys.stdin.readline())

    if (input == 1): 
        draw_circle(int(sys.argv[1]))
    elif (input == 2):
        draw_good_circle(int(sys.argv[1]))
    else: 
        print("Either choose 1 or 2 a option!")