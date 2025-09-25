numbers = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, numbers))

print(doubled)

even = list(filter(lambda x: x % 2==0, numbers))
print(even)

from functools import reduce

numbers = [1, 2, 3, 4]
sum_result = reduce(lambda x, y: x - y, numbers)

print(sum_result) 