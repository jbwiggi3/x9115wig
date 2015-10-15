import math

try:
	# see if Swampy is installed as a package
	from swampy.TurtleWorld import *
except ImportError:
	# otherwise see if the modules are on the PYTHONPATH
	from TurtleWorld import *


def draw(t, sides, radius):
	angle = 360.0 / sides
	for i in range(sides):
		triangle(t, radius, angle/2)
		lt(t, angle)

def triangle(t, radius, angle):
	y = radius * math.sin(angle * math.pi / 180)
	rt(t, angle)
	fd(t, radius)
	lt(t, 90 + angle)
	fd(t, 2 * y)
	lt(t, 90 + angle)
	fd(t, radius)
	lt(t, 180 - angle)

def move(t,radius):
	pu(t)
	fd(t, (radius * 2) + 20)
	pd(t)

world = TurtleWorld()
turtle = Turtle()
turtle.delay = 0
pu(turtle)
bk(turtle, 130)
pd(turtle)

for x in range(5,8):
	for z in range(x):
		draw(turtle, x, 8 * x - z * 8)
	if(x != 7):
		move(turtle, 8 * x)
die(turtle)

world.canvas.dump()

wait_for_user()