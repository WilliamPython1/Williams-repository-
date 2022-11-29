import turtle
import time
import random
red = turtle.Turtle()
blue = turtle.Turtle()
pink = turtle.Turtle()

    red.penup()
    red.goto(-200,-100)
    red.pendown()
    red.penup()
    red.goto(-200,-100)
    red.pendown()
    
for i in range(100):
    red.forward(5)
    time.sleep(random.randint(0,1))
    red.color('red')
    red.shape('turtle')
    red.speed(9)

    red.penup()
    red.goto(-200,-100)
    red.pendown()



    #



    blue.color('blue')
    blue.shape('turtle')
    blue.speed(9)

    blue.penup()
    blue.goto(-200,-120)
    blue.pendown()



    #




    pink.color('red')
    pink.shape('turtle')
    pink.speed(9)

    pink.penup()
    pink.goto(-200,-140)
    pink.pendown()




        

