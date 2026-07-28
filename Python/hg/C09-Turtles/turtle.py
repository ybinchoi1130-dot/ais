#Turtle

import turtle

t = turtle.Pen()

t.forward(100)
t.left(60)

t.forward(100)
t.right(45)

t.forward(100)
t.left(90)

t.forward(100)

turtle.done()

#%%%

import turtle
from random import randint
t= turtle.pen()

for x in randint(0, 500):
    t. forward(x)
    t. left(45)
    t. backward(x)
    t. right(90)
    
turtle.done()