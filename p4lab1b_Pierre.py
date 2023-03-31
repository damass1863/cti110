import turtle

# Set up the turtle

turtle.pensize(4)
turtle.color("pink")

# Draw the S
turtle.penup()
turtle.setpos(25,90)
turtle.pendown()

turtle.forward(20)
turtle.backward(20)

turtle.circle(-60, -180)
turtle.circle(60,-235)
turtle.pendown()

turtle.penup()
turtle.right(-60)
turtle.forward(160)
turtle.pendown()
turtle.circle(90,180)
turtle.left(90)
turtle.forward(250)
turtle.exitonclick()



    
