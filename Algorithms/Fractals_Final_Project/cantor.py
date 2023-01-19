def cantor(max_order=6, order=0, length=500, x=-100, y=0):
    if order == max_order:
        return
    
    if order == 0:
        length = max_order*80 # change size according to max order
        x = 0-length//2  # center it horizontally

    t.pu()
    t.goto(x,y)
    t.pd()
    t.width((max_order-order)*2)
    t.forward(length)
    cantor(max_order, order+1, length//3, x, y-20)
    cantor(max_order, order+1, length//3, x+((2/3)*length), y-20)


import turtle as t
t.speed('fastest')
t.hideturtle()
cantor(6)

## keeps turtle window open
t.exitonclick()