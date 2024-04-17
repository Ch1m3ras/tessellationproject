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
    for x in range(-1 * maxXRange, maxXRange, 330): #In order to change how close they are to each other, change the 3rd number (330 if you haven't edited it.) 
        for y in range(-1 * maxYRange, maxYRange, 199):
            tessalationTurtle.setheading(0)
            tessalationTurtle.penup()
            tessalationTurtle.goto(x, y)
            tessalationTurtle.pendown()
            buildBasicShape()

def buildColumnEven():
    for x in range(int((-1 * maxXRange) + 165), int(maxXRange - 165), 330): #In order to change how close they are to each other, change the 3rd number (330 if you haven't edited it.) and the + or minus numbers(+ 165 and - 165) (its just 1/2 of the 3rd number)
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
