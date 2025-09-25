#currying
def add(a,b):
    return a+b  

from functools import partial
add_5= partial(add,5)
print(add_5(10))
print(add_5(1))


def multiply(x,y,z,a):
    return x*y*z*a

partialmultiply=partial(multiply,2)

print(partialmultiply(3,4,5))

partialmultiply2=partial(multiply,2,3)
print(partialmultiply2(4,5))

def add1(a):
    def add2(b):
        def add3(c):
            return a+b+c        
        return add3
    return add2
fixed_add2=add1(2)
fixed_add2_add3= fixed_add2(3)
total= fixed_add2_add3(4)
 
print(fixed_add2)
print(fixed_add2(5))
print("------")
print(fixed_add2(5)(3))
print(add1(2)(3)(4))
print(total)   