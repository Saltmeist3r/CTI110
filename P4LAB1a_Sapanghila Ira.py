import turtle          
win = turtle.Screen()  
t = turtle.Turtle()

t.pensize(5)        
t.pencolor("Blue")     
t.shape("turtle")

t.forward(50)          
t.left(90)             
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)

t.penup()
t.forward(100)
t.pendown()

t.forward(100)          
t.left(120)            
t.forward(100)
t.left(120)
t.forward(100)



win.mainloop()
