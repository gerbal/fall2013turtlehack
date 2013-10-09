import turtle
import turtlehack

# Make a wide screen
turtle.setup(width=800)
test_turtle = turtle.Turtle()

# Reset function for in between tests
def reset(turtle):
  turtle.color('black')

# Moves turtle to x, y position
def move(turtle, x, y = 0):
  turtle.penup()
  turtle.setpos(x, y)
  turtle.pendown()

# Draws an X and prints that function_name is broken
def draw_error(function_name):
  test_turtle.write("x")
  print "-- Problem with " + function_name

# Prints "Testing" and the function name
def print_testing(function_name):
  print "Testing " + function_name
  test_turtle.penup()
  
  # Get y coordinates
  y = test_turtle.ycor()
  
  # Move turtle down 20, print function, then move back
  test_turtle.sety(y - 20)
  test_turtle.write(function_name, align="center", font=("Arial", 10, "normal"))
  test_turtle.sety(y + 20)
  test_turtle.pendown()

# random_color() test
move(test_turtle,-300,0)
try:
  print_testing("random_color()")
  test_turtle.color(turtlehack.random_color())
  test_turtle.circle(5)
  
except:
  draw_error("random_color()")

reset(test_turtle)

# colored_circle() test
move(test_turtle,-200,0)
try:
  print_testing("colored_circle()")
  turtlehack.colored_circle(test_turtle, 10, 'red')

except:
  draw_error("colored_circle()")

reset(test_turtle)

# colored_square() test
move(test_turtle,-100,0)
try:
  print_testing("colored_square()")
  turtlehack.colored_square(test_turtle, 20, 'blue')

except:
  draw_error("colored_square()")

reset(test_turtle)

# random_circle() test
move(test_turtle,0,0)
try:
  print_testing("random_circle()")
  test_turtle.color('green')
  turtlehack.random_circle(test_turtle, 5, 25)
except:
  draw_error("random_circle()")

reset(test_turtle)

# n_sided_polygon() test
move(test_turtle,100,0)
try:
  print_testing("n_sided_polygon()")
  turtlehack.n_sided_polygon(test_turtle, 8, "#99badd", 4, 15)
except:
  print "-- problem with n sided polygon()"

reset(test_turtle)

# random_location() test
move(test_turtle,220,0)
try:
  print_testing("random_location()")
  test_turtle.color('purple')
  turtlehack.random_location(test_turtle, 50, 50)
except:  
  draw_error("random_location()")

####################
print "End of tests"

reset(test_turtle)



turtle.done()
