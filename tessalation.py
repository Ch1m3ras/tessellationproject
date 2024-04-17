# **THIS WILL TAKE A LONG TIME TO RUN. I UNDERSTAND THAT YOU MAY THINK ITS CRASHED. IT DIDN'T IT JUST TAKES LIKE 2 MINUTES. THANK YOU FOR YOUR UNDERSTANDING.**
import turtle
maxXRange = 1000
maxYRange = 1000
screen = turtle.Screen()
screen.setup(maxXRange,maxYRange)
screen.tracer(0)
screen.colormode(255)
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
            colorX = x
            colorY = y
            if colorX > 255 or colorY > 255 or colorX < 0 or colorY < 0:
                while colorX > 255:
                    colorX = colorX - 255
                while colorY > 255:
                    colorY = colorY - 255
                while colorX < 0:
                    colorX = colorX + 255
                while colorY < 0:
                    colorY = colorY + 255
            tessalationTurtle.color((int(colorX), int(colorY), int((colorX + colorY) / 2)))
            tessalationTurtle.begin_fill()
            buildBasicShape()
            tessalationTurtle.end_fill()

def buildColumnEven():
    for x in range(int((-1 * maxXRange) + 172.5), int(maxXRange - 172.5), 345):
        for y in range(int((-1 * maxYRange) - 99.5), int(maxYRange + 140), 199):
            tessalationTurtle.setheading(0)
            tessalationTurtle.penup()
            tessalationTurtle.goto(x, y)
            tessalationTurtle.pendown()
            colorX = x
            colorY = y
            if colorX > 255 or colorY > 255 or colorX < 0 or colorY < 0:
                while colorX > 255:
                    colorX = colorX - 255
                while colorY > 255:
                    colorY = colorY - 255
                while colorX < 0:
                    colorX = colorX + 255
                while colorY < 0:
                    colorY = colorY + 255
            tessalationTurtle.color((int(colorX), int(colorY), int((colorX + colorY) / 2)))
            tessalationTurtle.begin_fill()
            buildBasicShape()
            tessalationTurtle.end_fill()
    

buildColumnOdd()
buildColumnEven()


#This is just to make sure it stays on the screen with VS Code, you may disregard it. 
input()
