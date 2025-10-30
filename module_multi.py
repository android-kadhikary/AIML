import sys, random as rn, functools
from enum import Enum, auto

# print(rn.random())# between 0.0 and 1.0
# print(rn.randint(1,10))
# elements=["red", " blue", "green"]
# print(rn.choice(elements))
# rn.shuffle(elements)
# print(elements)

# sys : methods and parameters to ineract with Python runtime environment
# print ("script name ",sys.argv[0])
# print ("script name ",sys.path)
# sys.exit("exit the script")

#functools.partial : generate a new fuction after fixing some arg of a funtion
def sum(a,b):
    return a+b

add_with_10=functools.partial(sum, 10)
print(add_with_10(2))

number=[1,2,3,4]
# apply a function cumulatively to the item of an iterable

print(functools.reduce(lambda x, y : x+y, number))

# enum : group togater related contants in human readable form, it's iterable, Hashable, immitable

class Status(Enum):
    ACTIVE = auto()
    INACTIVE = auto()
    CLOSE = auto()
   

print (Status.ACTIVE.value) # get individual values
print (list(Status))    

class Do_math(Enum):
    MUL = "multiply"
    ADD = "+"
    SUB = "-"

    def perform(self, a, b):
        if self == Do_math.ADD:
            return a+b
        elif self == Do_math.SUB:
            return a-b
        elif self == Do_math.MUL:
            return a*b
        
print(Do_math.ADD.perform(1,4))        