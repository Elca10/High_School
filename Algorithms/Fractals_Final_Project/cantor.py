# DEFINING THE FUNCTION
# Parameter key
#   - max_order: user can set a maximum fractal depth, defaults to 4
#   - order: keeps track of depth (or the 'order' of the fractal), starts at 0
#   - length: controls size of triangle (side length)
def cantor(max_order=6, order=0, length=None, x=None, y=0):
    # BASE CASE
    if order == max_order:
        return
    
    # INITIAL SETUP
    if order == 0:
        # if the user hasn't set a length...
        if not length:
            # ... change line size based on max order
            length = max_order*80 
        # if the user hasn't set an x coord...
        if not x:
            # ... use the length to horizontally center the fractal
            x = 0-length//2 

    # DRAWING THE LINE
    ## Line setup
    t.pu()
    t.goto(x,y)
    t.pd()
    t.width((max_order-order)*2)
    ## Draw the line
    t.forward(length)

    # RECURSIVE CALLS
    ## Left third
    cantor(max_order, order+1, length//3, x, y-20)
    ## Right third
    cantor(max_order, order+1, length//3, x+((2/3)*length), y-20)


# DRAWING THE CANTOR SET FRACTAL
## Turtle setup and fractal function call
import turtle as t
t.speed('fastest')
t.hideturtle()
t.setheading(0)
cantor()

## keeps turtle window open
t.exitonclick()