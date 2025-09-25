
sq =lambda x: x*x
print(sq(5))

new_sq_ =map (lambda x: x*2, [1,2,3,4,5])
print(set(new_sq_))

new_sq_filter= filter(lambda x: x%2==0, [1,2,3,4,5])
print(list(new_sq_filter))

from functools import reduce
new_sq_reduce= reduce(lambda x,y: x+y, [1,2,3,4,5])
print(new_sq_reduce)


#comparison
print( (lambda x,y: x if x>y else y)(5,10) )