# **THIS WILL TAKE A LONG TIME TO RUN. I UNDERSTAND THAT YOU MAY THINK ITS CRASHED. IT DIDN'T IT JUST TAKES LIKE 2 MINUTES. THANK YOU FOR YOUR UNDERSTANDING.**
import turtle
maxXRange = 1000
maxYRange = 1000
screen = turtle.Screen()
screen.setup(maxXRange,maxYRange)
screen.tracer(0)
tessalationTurtle = turtle.Turtle()

def buildBasicShape():
    for x in range(0, 901):
        tessalationTurtle.forward(0.1)
        tessalationTurtle.left(0.1)
    tessalationTurtle.right(180)
    for x in range(0, 901):
        tessalationTurtle.forward(0.1)
        tessalationTurtle.left(0.1)
    tessalationTurtle.right(60)
    for x in range(0, 901):
        tessalationTurtle.forward(0.1)
        tessalationTurtle.right(0.1)
    tessalationTurtle.right(180)
    for x in range(0, 901):
        tessalationTurtle.forward(0.1)
        tessalationTurtle.right(0.1)
    tessalationTurtle.right(60)
    for x in range(0, 901):
        tessalationTurtle.forward(0.1)
        tessalationTurtle.left(0.1)
    tessalationTurtle.right(180)
    for x in range(0, 901):
        tessalationTurtle.forward(0.1)
        tessalationTurtle.left(0.1)
    tessalationTurtle.right(60)
    for x in range(0, 901):
        tessalationTurtle.forward(0.1)
        tessalationTurtle.right(0.1)
    tessalationTurtle.right(180)
    for x in range(0, 901):
        tessalationTurtle.forward(0.1)
        tessalationTurtle.right(0.1)
    tessalationTurtle.right(60)
    for x in range(0, 901):
        tessalationTurtle.forward(0.1)
        tessalationTurtle.left(0.1)
    tessalationTurtle.right(180)
    for x in range(0, 901):
        tessalationTurtle.forward(0.1)
        tessalationTurtle.left(0.1)
    tessalationTurtle.right(60)
    for x in range(0, 901):
        tessalationTurtle.forward(0.1)
        tessalationTurtle.right(0.1)
    tessalationTurtle.right(180)
    for x in range(0, 901):
        tessalationTurtle.forward(0.1)
        tessalationTurtle.right(0.1)

def buildColumnOdd():
    for x in range(-1 * maxXRange, maxXRange, 345):
        for y in range(-1 * maxYRange, maxYRange, 199):
            tessalationTurtle.setheading(0)
            tessalationTurtle.penup()
            tessalationTurtle.goto(x, y)
            tessalationTurtle.pendown()
            buildBasicShape()

def buildColumnEven():
    for x in range(int((-1 * maxXRange) + 172.5), int(maxXRange - 172.5), 345):
        for y in range(int((-1 * maxYRange) - 99.5), int(maxYRange + 140), 199):
            tessalationTurtle.setheading(0)
            tessalationTurtle.penup()
            tessalationTurtle.goto(x, y)
            tessalationTurtle.pendown()
            buildBasicShape()
    

buildColumnOdd()
buildColumnEven()


#This is just to make sure it stays on the screen with VS Code, you may disregard it. 
input()
