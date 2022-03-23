class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # String representation
    def __repr__(self):
        return f"Point(x={self.x}, y={self.y}, z={self.z})"

    # Modify Dunder Method
    def __eq__(self, other):
        # Check if only comparing with another Point object
        if isinstance(other, Point):
            return (self.x, self.y, self.z) == (other.x, other.y, other.z)
        return NotImplemented


p1 = Point(1, 2, 3)
print(p1)
p2 = Point(1, 2, 3)
print(p1.__eq__(p2))
