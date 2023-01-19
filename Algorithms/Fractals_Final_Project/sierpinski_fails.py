
# TURTLE SETUP
import turtle as t
t.hideturtle()
t.penup()
t.speed('fastest')
t.goto(0,0)
t.pendown()

# SIERPINSKI'S TRIANGLE
def triangle(max_order=4, order=0, length=200, x=0,y=0, angle=0): # change x and y so better starting pos in turtle
    if order > max_order:
        return
    elif isinstance(length, int) == False: # so small that lengths are no longer whole numbers
        return
    if order==0:
        length = max_order*10
    #    t.fillcolor('black')
    #else:
    #    t.fillcolor('white')

    t.pu()
    t.hideturtle()
    t.goto(x, y)
    t.pd()

    # draw triangle
    #t.begin_fill()
    coords = []
    for i in range(3):
        t.setheading(angle)
        t.forward(length)
        coords.append((t.xcor(), t.ycor()))
        if order == 0:
            angle += 120
        else:
            angle -= 120
    #t.end_fill()
    
    order += 1
    
    # find midpoints using coords, then set those for x and y (and/or the 1/2 thing from the website). 
    x = t.xcor()
    y = t.ycor()
    triangle(max_order, order, length/2, x, y, angle) # x, y, angle need to change
    triangle(max_order, order, length/2, x, y, angle)




def triangle1(max_order=4, order=0, length=400, x=0, y=0, angle=0):
    time.sleep(0.1)
    if order > max_order:
        return
    elif isinstance(length, int) == False: # so small that lengths are no longer whole numbers
        return
    if order==0:
        length = max_order*100
    
    t.pu()
    t.hideturtle()
    t.goto(x, y)
    t.pd()

    coords = []
    for i in range(3):
        t.setheading(angle)
        t.forward(length)
        coords.append((t.xcor(), t.ycor()))
        if order == 0:
            angle += 120
        else:
            angle -= 120
    #t.end_fill()
    
    # then draw the triangle at the first and second coords listed  # AT MIDPOINTS
    #
    x1, y1 = coords[0]
    x2, y2 = coords[1]
    x3, y3 = coords[2]
    midx1, midy1 = (x1+x2)//2, (y1 +y2)//2
    midx2, midy2 = (x2+x3)//2, (y2 +y3)//2
    midx3, midy3 = (x3+x1)//2, (y3 +y1)//2

    order += 1
    length = length//2
    #triangle1(max_order, order, length, midx1, midy1)
    if order == 1:
        angle = angle + 60
    triangle1(max_order, order, length, midx2, midy2, angle-120)
    #triangle1(max_order, order, length, midx3, midy3)


import time
    
#triangle1(3)
#time.sleep(10)



def triangle3(max_order=4, order=0, length=400, x=-250, y=0, angle=0):
    if order > max_order:
        return
    if length <=1:
        return
    
    t.hideturtle()
    #for i in range(3):
    order += 1
    t.pu()
    t.goto(x,y)
    t.pd()
    for i in range(3):
        t.setheading(angle)
        t.forward(length)
        if i == 0:
            t.backward(length)
            angle += 60
        else:
            angle -= 120
    triangle3(max_order, order, length//2, x, y, angle)
    '''
    t.pu()
    t.goto(x, y)
    t.setheading(angle + 60)
    t.pd()
    t.forward(length)
    triangle3(max_order, order, length//2, t.xcor(), t.ycor(), angle)

    t.pu()
    t.goto(x, y)
    t.setheading(angle + 60)
    t.pd()
    t.forward(length)
    triangle3(max_order, order, length//2, t.xcor(), t.ycor(), angle)
    '''




def triangle2(max_order=4, order=0, length=50, x=0, y=0, angle=0):
    time.sleep(0.2)
    if order > max_order:
        return
    elif isinstance(length, int) == False: # so small that lengths are no longer whole numbers
        return
    if order==0:
        length = max_order*20
    
    t.pu()
    t.hideturtle()
    t.goto(x, y)
    t.pd()

    t.fillcolor('red')
    t.begin_fill()
    coords = []
    for i in range(3):
        t.setheading(angle)
        t.forward(length)
        coords.append((t.xcor(), t.ycor()))
        if order == 0:
            angle += 120
        else:
            angle -= 120
    t.end_fill()
    
    # then draw the triangle at the first and second coords listed  # AT MIDPOINTS
    #
    x1, y1 = coords[0]
    x2, y2 = coords[1]
    x3, y3 = coords[2]
    for x, y in coords:
        t.pu()
        t.goto(x, y)
        t.pd()
        angle = 0
        for i in range(3):
            t.setheading(angle)
            t.forward(length)
            angle +=120

    order += 1
    length = length//2

#triangle3(15)
#time.sleep(10)





def triangle4(length, depth):
    if depth == 0:
        t.pd()
        #t.stamp()
        t.forward(length)
        t.left(120)
        t.forward(length)
        t.left(120)
        t.forward(length)

        t.pu()
        return
    else:
        t.pu()
        for i in range(3):
            t.forward(length)
            triangle4(length/2, depth-1)
            t.backward(length)
            t.left(120)

t.speed('fastest')
t.right(30)
t.shape('triangle')
t.hideturtle()
#triangle4(200,3)
#time.sleep(10)


def triangle5(max_order, order, length=0):
    if order < max_order:
        # draw triangle
        t.pd()
        t.forward(length)
        t.left(120)
        t.forward(length)
        t.left(120)
        t.forward(length)
        t.pu()
        return
    if order == 0:
        length = max_order**2
    



def make_triangle(length=300,x=500,y=-500):
    coords = [(x,y)]
    t.setheading(120)
    for i in range(3):
        t.pu()
        t.forward(length)
        t.left(120)
        t.pd()
        t.dot(5, 'red')
        coords.append((t.xcor(), t.ycor()))
    t.pu()
    return coords

def chaos(coords, x, y, i=0):
    if i == 100:
        return
    x2, y2 = coords[r.randint(0, len(coords)-1)] # chooses another random coordinate
    new_x, new_y = (x + x2)//2, (y + y2)//2
    t.pu()
    t.goto(new_x, new_y)
    t.pd()
    t.dot(5, 'black')
    chaos(coords, new_x, new_y, i + 1)

import random as r
'''
coords = make_triangle()
#x, y = (r.randint(-400,500), r.randint(-500,-400))
x, y = -250, 100
coords.append((x,y))
chaos(coords, x, y)
time.sleep(10)
'''


def sierpinski(max_order=4, order=0, length=200):
    # base case
    if order == max_order:
        # draw triangle
        for i in range(3):
            t.forward(length)
            t.left(120)
        return 
    

    x,y = t.xcor(), t.ycor()

    # recursive call (bottom left mini triangle)
    sierpinski(max_order, order+1, length//2)
    t.goto(x+(length//2), y)

    # recursive call (bottom right mini triangle)
    sierpinski(max_order, order+1, length//2)
    t.goto(x+(length//4), y+(((3**(1/2))/4)*length))

    # recursive call (top mini triangle)
    sierpinski(max_order, order+1, length//2)
    t.goto(x, y)

t.pencolor('red')
t.setheading(0)
sierpinski()
## keeps turtle window open
t.exitonclick()