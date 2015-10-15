try:
    # see if Swampy is installed as a package
    from swampy.TurtleWorld import *
except ImportError:
    # otherwise see if the modules are on the PYTHONPATH
    from TurtleWorld import *

from polygon import *


def flower(t, n, radius, angle):
    for i in range(n):
        for j in range(2):
            arc(t, radius, angle)
            lt(t, 180-angle)
        lt(t, 360.0/n)


def move(t, length):
    pu(t)
    fd(t, length)
    pd(t)


world = TurtleWorld()
turtle = Turtle()
turtle.delay = 0.001

move(turtle, -100)
flower(turtle, 7, 50.0, 60.0)

move(turtle, 100)
flower(turtle, 10, 40.0, 80.0)

move(turtle, 100)
flower(turtle, 20, 120.0, 20.0)

die(turtle)

world.canvas.dump()

wait_for_user()