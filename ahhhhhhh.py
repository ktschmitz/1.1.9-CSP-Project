import turtle


#set up screen
wn = turtle.Screen()
wn.title("Catching Fruit")
turtle.bgpic("finalamazon1.png")

# turtle object
img_turtle = turtle.Turtle()

# registering the image
# as a new shape

turtle.register_shape('basket4.gif')
turtle.speed(0)
turtle.penup()
turtle.goto(0,-350)

wn.mainloop()
