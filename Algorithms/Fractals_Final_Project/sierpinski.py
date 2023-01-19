
def sierpinski(max_order=4, order=0, length=200):
    # base case
    if order == max_order:
        # draw triangle
        for i in range(3):
            t.forward(length)
            t.left(120)
        return 
    
    x,y = t.xcor(), t.ycor()

    # recursive call (bottom left triangle)
    sierpinski(max_order, order+1, length//2)
    t.goto(x+(length//2), y)

    # recursive call (bottom right triangle)
    sierpinski(max_order, order+1, length//2)
    t.goto(x+(length//4), y+(((3**(1/2))/4)*length))

    # recursive call (top triangle)
    sierpinski(max_order, order+1, length//2)
    t.goto(x, y)

import turtle as t
import time

t.pencolor('red')
t.setheading(0)
sierpinski()

## keeps turtle window open
t.exitonclick()