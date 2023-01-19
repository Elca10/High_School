import turtle as t
t.pendown()
t.pencolor('blue')
#t.forward(100)
t.fillcolor('red')
print(t.heading())
t.begin_fill()
angle = 0 # 90+30 (60 degree angle from x axis)
length = 100
for i in range(3):
    t.setheading(angle)
    t.forward(length)
    angle += 120
t.end_fill()

import time
time.sleep(10)