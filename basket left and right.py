import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgpic("finalamazon1.png")
screen.setup(width=800, height=600)
screen.tracer(0)  # Turn off automatic screen updates

# Register the image as a new shape
turtle.register_shape('basket4.gif')

# Create the basket
basket = turtle.Turtle()
basket.shape('basket4.gif')
basket.penup()
basket.speed(0)
basket.goto(0, -250)

# Create the fruit
fruit = turtle.Turtle()
fruit.shape("circle")
fruit.color("red")
fruit.penup()
fruit.speed(0)
fruit.goto(0, 250)

# Set the gravity for the fruit
gravity = 0.2
fruit_dy = 0

# Define movement functions for the basket
basket_speed = 20
basket_dx = 0

def move_right():
    global basket_dx
    basket_dx = basket_speed

def move_left():
    global basket_dx
    basket_dx = -basket_speed

def stop_movement():
    global basket_dx
    basket_dx = 0

# Bind the movement functions to keyboard keys
screen.listen()
screen.onkeypress(move_right, 'Right')
screen.onkeypress(move_left, 'Left')
screen.onkeyrelease(stop_movement, 'Right')
screen.onkeyrelease(stop_movement, 'Left')

# Function to move the basket smoothly
def move_basket_smooth():
    global basket_dx
    x = basket.xcor()
    x += basket_dx
    if x > 380:
        x = 380
    elif x < -380:
        x = -380
    basket.setx(x)
    screen.update()
    screen.ontimer(move_basket_smooth, 20)

# Function to move the fruit continuously
def move_fruit():
    global fruit_dy
    y = fruit.ycor()
    y -= fruit_dy
    fruit.sety(y)
    fruit_dy += gravity
    if y < -300:
        reset_fruit()
    if abs(basket.xcor() - fruit.xcor()) < 50 and abs(basket.ycor() - fruit.ycor()) < 20:
        reset_fruit()

    screen.update()
    screen.ontimer(move_fruit, 10)

# Function to reset the fruit position
def reset_fruit():
    global fruit_dy
    fruit.goto(random.randint(-380, 380), 250)
    fruit_dy = 0

# Start the game
screen.update()
move_basket_smooth()
move_fruit()

# Start the main event loop
screen.mainloop()
