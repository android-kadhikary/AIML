#use of Super() method 
# class Parent:
#     def __init__(self):
#         self.name = "Parent"


#     def show_name(self):
#         return (self.name)
    
# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         #self.name = "Child"
#         self.info = "Child info"
#     def show_name(self):
#         print (super().show_name())
#         print(self.name + " overridden in Child")

# child_object = Child()
# child_object.show_name()

#operator over loading 1
class Number:
    def __init__(self,value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)
    
    def __str__(self):
        return f"Point({self.value})"
    
n1 = Number(10)
n2 = Number(20)
print(n1+n2)    
#print (N1(10)+N1(20))
print("operator over loading 2")
#operator over loading 2
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

# Usage
p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2  # Uses __add__ method
print(p3)


#method overloading
class Calculator:
    def add(self, a, b, c=0): #this method is overloaded with default parameter
        return a + b + c

calc = Calculator()
print(calc.add(2, 3))    # Output: 5
print(calc.add(2, 3, 5)) # Output: 10