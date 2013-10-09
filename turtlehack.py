import turtle
import random

# A function that takes a turtle, a radius, a color, and an optional thickness and draws a circle
def colored_circle(turtle, radius, color, thickness = 1):
	turtle.width(thickness)
	turtle.color(color)
	turtle.circle(radius)


# A function that takes a side length and a color and makes a square. 
#ef colored_square(turtle, side_length, color):
	# TODO: write this function 

# A function that takes a number and makes that many random sized circles
def random_circle(turtle, number_of_circles, max_size = 100):
	for i in range(number_of_circles):
	  turtle.circle(random.randint(0,max_size + 1))


# A function that changes the turtle's color to a random color
def random_color():
	'''
	returns a random hex value
	'''
	color_value = format(random.randint(0,16777215),'06x')
	return "#" +color_value

# A function that takes a turtle and a pair of numbers and sets the turtle to a random location from x to -x and y to -y

def random_location(turtle, x, y):
	'''
	Moves turtle to random location within bounds (-x,-y) and (x,y)
	takes arguments turtle, x, and y
	'''
	rand_x = -x + random.randint(0,2*x)
	rand_y = -y + random.randint(0,2*y)
	turtle.setpos(rand_x, rand_y)

#def random_location(turtle, x, y):
	# TODO: write this function 


# A function that draws an n-sided polygon
def n_sided_polygon(turtle, n, color="#FFFFFF", line_thickness=1, line_length=80):
	'''
	Draw an n-sided polygon
	input: turtle, number of sides, line color, line thickness, line length
	'''
	# for n times:
	# Draw a line, then turn 360/n degrees and draw another

	# set initial parameters
  	turtle.degrees()
  	turtle.pensize(line_thickness)
  	turn_angle = (360/n)

	# Draw each line segment and turn

  	for i in range(0,n):
	  turtle.color(color)
    	  turtle.pendown()
    	  turtle.forward(line_length)
   	  turtle.penup()
    	  turtle.left(turn_angle)

	# return the turtle to its original starting location
	turtle.left(turn_angle)

	return 0


