# DEFINING THE FUNCTION
# Parameter key
#   - max_order: user can set a maximum fractal depth, defaults to 4
#   - order: keeps track of depth (or the 'order' of the fractal), starts at 0
#   - angle, x, y, and length: these vars give information about the lines to be drawn
def canopy(max_order=4, order=0, angle=90, x=0, y=-250, length=20):
    # BASE CASE
    if order > max_order:
        return 
    

    # PREPARING TO DRAW LINE
    ## Sets a starting length based on the maximum order depth
    if order==0:
        length = 10*max_order

    ## Turtle moves to position
    t.pu()
    t.hideturtle()
    t.goto(x, y)
    t.pd()

    ## Sets color (lines will become more green around the edges)
    t.colormode(255)
    t.pencolor((0, 255//(((max_order-order)//2)+1), 0))


    # DRAW LINE
    t.setheading(angle)
    t.forward(length)


    # RECURSIVE CALLS
    ## Increases depth (order) by 1 and gets current turtle coords
    order += 1
    x = t.xcor()
    y = t.ycor()

    ## 1 recursive call for each branch (1 line --> 2 new lines (Y shape))
    canopy(max_order, order, angle-20, x, y, length-10)
    canopy(max_order, order, angle+20, x, y, length-10)


# DRAWING THE TREE
## Turtle setup and tree function call
import turtle as t
t.speed('fastest')
t.hideturtle()
canopy(10)

## keeps turtle window open
t.exitonclick()
