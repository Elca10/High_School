# DEFINING THE FUNCTION
# Parameter key
#   - max_order: user can set a maximum fractal depth, defaults to 4
#   - order: keeps track of depth (or the 'order' of the fractal), starts at 0
#   - length: controls size of triangle (side length)
def sierpinski(max_order=4, order=0, length=200):
    # BASE CASE
    if order == max_order:
        # draw triangle
        for i in range(3):
            t.forward(length)
            t.left(120)
        return 
    
    # RECURSIVE PART
    ## Save current coordinates
    x,y = t.xcor(), t.ycor()

    ## 1st recursive call (bottom left triangle)
    sierpinski(max_order, order+1, length//2)
    t.goto(x+(length//2), y)

    ## 2nd recursive call (bottom right triangle)
    sierpinski(max_order, order+1, length//2)
    t.goto(x+(length//4), y+(((3**(1/2))/4)*length))

    ## 3rd recursive call (top triangle)
    sierpinski(max_order, order+1, length//2)
    t.goto(x, y)


# DRAWING THE TRIANGLE FRACTAL
## Turtle setup and fractal function call
import turtle as t
t.speed('fastest')
t.hideturtle()
t.setheading(0)
sierpinski()

## keeps turtle window open
t.exitonclick()