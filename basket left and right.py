import turtle
import random
import keyboard
wn = turtle.Screen()
turtle.bgpic("finalamazon1.png")
wn.setup(width=800, height=600)
last_pressed = 'up'

turtleX = 0

# registering the image
# as a new shape
turtle.register_shape('basket4.gif')
turtle.shape('basket4.gif')

def f1():
  global turtleX
  turtleX += 10

def f2():
  global turtleX
  turtleX -= 10

# Basket on bottom
def setup(col, x, y, w, s, shape):
  turtle.penup()
  turtle.up()
  turtle.goto(0,-350)
  turtle.width(w)
  turtle.turtlesize(s)
  turtle.color(col)
  turtle.lt(90)
  turtle.down()
  turtle.penup()

  keyboard.add_hotkey('d', fun1())
  keyboard.add_hotkey('a', fun2())
  '''
  wn.onkey(quitTurtles, "Escape")
  '''
  wn.listen()
  wn.mainloop()
  turtle_scale = .5

#Event handlers
def right():
  global last_pressed
  if last_pressed == 'left':
    turtle.fd(10)
  elif last_pressed == 'right':
    turtle.lt(180)
    turtle.fd(10)
  else:
    turtle.rt(90)
    turtle.fd(10)

  last_pressed = 'left'

def left():
  global last_pressed
  if last_pressed == 'left':
    turtle.rt(180)
    turtle.fd(10)
  elif last_pressed == 'right':
    turtle.fd(10)
  else:
    turtle.lt(90)
    turtle.fd(10)

  last_pressed = 'right'


#add the fruit
fruit = turtle.Turtle()
fruit.speed(0)
fruit.shape("circle")
fruit.color("red")
fruit.penup()
fruit.goto(0,350)

while True:
    turtle.goto(turtleX,-350)
    wn.update()

    y =  fruit.ycor()
    y-=3
    fruit.sety(y)
    
    #check if off the screen
    if y < -300:
      x = random.randint(-380, 380)
      y = random.randint(300,400)
      fruit.goto(x,y)

    #check for a collision with the player
    if turtle.distance(fruit) < 20:
      x = random.randint(-380, 380)
      y = random.randint(300,400)
      fruit.goto(x,y)

  

'''
def quitTurtles():
  wn.bye()

setup("blue",-200,200,2,2,"turtle")
'''