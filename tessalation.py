import turtle
maxXRange = 1000
maxYRange = 1000
screen = turtle.Screen()
screen.setup(maxXRange,maxYRange)
screen.tracer(0)
tessalationTurtle = turtle.Turtle()

def buildBasicShape():
    for x in range(0, 901):
        tessalationTurtle.forward(.1)
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

def buildColumn(x):
    for y in range(-1 * maxYRange, maxYRange, 199):
        tessalationTurtle.setheading(0)
        tessalationTurtle.penup()
        tessalationTurtle.goto(x, y)
        tessalationTurtle.pendown()
        buildBasicShape()

buildColumn(0)


#This is just to make sure it stays on the screen with VS Code, you may disregard it. 
input()
