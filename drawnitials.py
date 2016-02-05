import turtle

window = turtle.Screen()
turtle.Turtle()
turtle.bgcolor("red")

#for alphabet M
turtle.pu()  # pen up
turtle.setpos(-300,0)
turtle.seth(90)
turtle.pd()
turtle.forward(200)
turtle.right(165)
turtle.forward(150)
turtle.left(150)
turtle.forward(150)
turtle.seth(270)
turtle.forward(200)
turtle.pu()


#for alphabet A
turtle.pu()
turtle.setpos(-200,0)
turtle.pd()
turtle.seth(0)
turtle.left(75)
turtle.forward(200)
turtle.right(150)
turtle.forward(200)

turtle.right(180)
turtle.forward(80)
turtle.seth(180)
turtle.forward(62)
turtle.pu()

turtle.setpos(100,0)
turtle.pd()

for i in range(1,37):  #draw petals
    turtle.left(35)
    turtle.forward(50)
    turtle.right(35)
    turtle.forward(50)
    turtle.right(145)
    turtle.forward(50)
    turtle.right(35)
    turtle.forward(50)
    turtle.right(10)
turtle.seth(270) #set heading south (270)
turtle.forward(200) #draw the flower tail


window.exitonclick()


