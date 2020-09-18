import turtle
def width(x):
    turtle.forward(300)
    turtle.penup()
    turtle.goto(0,60*(x+1))
    turtle.pendown()
def height(x):
    turtle.forward(300)
    turtle.penup()
    turtle.goto(60*(x+1),0)
    turtle.pendown()
x=0
while (x<6):
   width(x)
   x=x+1
x=0
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.setheading(90)
while (x<6):
   height(x)
   x=x+1

turtle.exitonclick()
