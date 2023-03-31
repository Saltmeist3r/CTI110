import turtle

t = turtle.Turtle()

t.pencolor("blue")
t.pensize(5)
t.shape("turtle")

t.left(90)
t.forward(100)
t.penup()
t.left(180)
t.forward(50)
t.pendown()
t.left(90)

t.penup()
t.forward(50)
t.pendown()

t.circle(25, 180)
t.down()
t.circle(-25, 180)
t.right(180)


turtle.done()
