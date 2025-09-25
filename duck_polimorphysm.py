import math
def get_area(shape):
    shape.area()

class Circle:
    def __init__(self, redious):
        self.redious = redious  

    def area(self):
        print("Area of Circle:", math.pi * self.redious * self.redious)   

class Square:
    def __init__(self, side):
        self.side = side  

    def area(self):
        print("Area of Square:", self.side * self.side)

circle = Circle(5)
square = Square(4)

get_area(circle)  # Output: Area of Circle: 78.53981633974483
get_area(square)  # Output: Area of Square: 16