# str() & int() are classes not functions
# self is always passed in as the first argument - variable that points to the instance of our class
# you can call the self variable anything

import math


class Circle:
    """
    Return the parameters of a Circle given the radius
    """
    def __init__(self, radius=1):
        self.radius = radius

    # convert to programmer readable string representation.
    def __repr__(self):
        return f"Circle({self.radius})"

    @property
    def diameter(self):
        return self.radius * 2

    @property
    def area(self):
        return self.radius**2 * math.pi


c = Circle(5)
print(c.radius)
print(c.diameter)
print(c.area)

c = Circle(2)
print(c.radius)
print(c.diameter)
print(c.area)