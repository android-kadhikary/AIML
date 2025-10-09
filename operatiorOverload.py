class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Operator Overloading: Defines the behavior of the '+' operator
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def __sub__(self, other1):
        return Vector(self.x - other1.x, self.y - other1.y)
v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2  # Calls v1.__add__(v2)
print(v3.x, v3.y)
# v3 is now a new Vector(4, 6)

v4= v1 - v2  # Calls v1.__sub__(v2)
# v4 is now a new Vector(-2, -2)
print(v4.x, v4.y)


tup1=(1,2)
tup2=(15,7)

tupR=tup1 + tup2
tup_zip=zip(tup1, tup2)
print(tuple(tup_zip))