import turtle as t

def tree(max_order=4, order=0, angle=90, x=0, y=-250, length=20):
    if order==0:
        length = 10*max_order
    if order > max_order:
        return 

    t.pu()
    t.hideturtle()
    t.goto(x, y)
    t.pd()
    '''
    if order %2 ==0:
        t.color('blue')
    else:
        t.color('red')
    '''
    t.colormode(255)
    t.pencolor((0, 255//(((max_order-order)//2)+1), 0))
    t.setheading(angle)
    t.forward(length)

    #print(order)
    order += 1
    
    x = t.xcor()
    y = t.ycor()
    tree(max_order, order, angle-20, x, y, length-10)
    tree(max_order, order, angle+20, x, y, length-10)
    #t.backward(length)
    
t.speed('fastest')
#s = t.getscreen()
#import time
#time.sleep(10)
tree(10)
