import turtle
import math

levi=turtle.Turtle()
levi.speed(10)
for i in range(2000):
    levi.forward(math.sqrt(i))
    levi.left(i%100)
turtle.done()