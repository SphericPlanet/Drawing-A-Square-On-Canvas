import turtle

turtle.title("A Square On Canvas")

screen = turtle.Screen()
screen.bgcolor("Cyan")

##Turtle
t = turtle.Turtle()
t.pencolor("Green")
t.shape("turtle")
t.pensize(5)
t.speed(1)
t.fillcolor("Red")

t.begin_fill()
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.end_fill()

turtle.done()