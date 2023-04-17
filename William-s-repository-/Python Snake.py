import turtle
import random
t = turtle.Turtle()
t.speed(0)
turtle.listen()
colourCycle = 0
global colourCycle
def forward():
    t.forward(10)
def backward():
    t.backward(10)
def left():
    t.left(10)
def right():
    t.right(10)
def colour():
    colours = ["Red", "Yellow", "Blue"]
    colourCycle = colourCycle + 1
    t.color = colours[colourCycle]
    
turtle.onkeypress(forward, "Up")
turtle.onkeypress(backward, "Down")
turtle.onkeypress(left, "Left")
turtle.onkeypress(right, "Right")
turtle.onkeypress(colour, "c")



    

