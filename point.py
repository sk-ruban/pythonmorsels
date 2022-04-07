class Point:
    """ 3-D Point """
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # String representation
    def __repr__(self):
        return f"Point(x={self.x}, y={self.y}, z={self.z})"

    # Modify Dunder Method for equality
    def __eq__(self, other):
        # Check if only comparing with another Point object
        if isinstance(other, Point):
            return (self.x, self.y, self.z) == (other.x, other.y, other.z)
        return NotImplemented

    # Bonus 1 - Addition & Subtraction
    # p1 + p2 is equivalent to p1.__add__(p2)
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)

    # Bonus 2 - Multiplication
    # Dot Product
    def __mul__(self, scale):
        return Point(scale * self.x, scale * self.y, scale * self.z)

    # Scalar Multiplication -> rmul means multiply from the right
    def __rmul__(self, scale):
        return Point(scale * self.x, scale * self.y, scale * self.z)

    # Bonus 3 - Tuple unpacking
    def __iter__(self):
        return iter((self.x, self.y, self.z))


p1 = Point(1, 2, 3)
print(p1)
p2 = Point(1, 2, 3)
print(p1.__eq__(p2))
p2 = Point(4, 5, 6)
print(p1 + p2)
print(p1 - p2)
print(p1 * 2)
print(3 * p1)
x, y, z = p1
print(x)