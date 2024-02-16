import turtle

wn = turtle.Screen()

turtle.bgpic("finalamazon1.png")

last_pressed = 'up'


# create two empty lists of turtles, adding to them later
horiz_turtles = []
vert_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic", "arrow", "turtle", "circle", "square", "triangle", "classic"]

vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown", "darkred", "darkblue", "lime", "salmon", "indigo", "brown"]


def setup(col, x, y, w, s, shape):
  turtle.penup()
  turtle.up()
  turtle.goto(0,-400)
  turtle.width(w)
  turtle.turtlesize(s)
  turtle.color(col)
  turtle.shape(shape)
  turtle.lt(90)
  turtle.down()
  turtle.penup()
  wn.listen()

turtle_image = "basket2.gif"
wn.addshape(turtle_image)

setup("blue", -200, 200, 2, 2, "turtle")

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
  global turtle
  if last_pressed == 'left':
    turtle.rt(180)
    turtle.fd(10)
  elif last_pressed == 'right':
    turtle.fd(10)
  else:
    turtle.lt(90)
    turtle.fd(10)

  last_pressed = 'right'

wn.onkey(left(), "Left")
wn.onkey(right(), "Right")


tloc = -500
for s in turtle_shapes:
  
  # Make vertical turtles and change the colors for each shape
  vt = turtle.Turtle(shape=s)
  vert_turtles.append(vt)
  vt.penup()
  new_color = vert_colors.pop()
  vt.fillcolor(new_color)
  vt.goto( tloc, 400)
  vt.setheading(270)
  # Spacing between shapes
  tloc += 80

# TODO: move turtles across and down screen, stopping for collisions

for step in range(1000):
  # for each horizontal turtle
  for vt in vert_turtles:
    vt.forward(50)
  


wn.mainloop()
