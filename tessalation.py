import turtle
screen = turtle.Screen()
screen.setup(1000,1000)
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

buildBasicShape()
