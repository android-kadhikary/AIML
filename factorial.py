def factorial(number):
    factorial_of_number=0
    if number<=1: # this  i sthe base case
        return 1
    else:
        factorial_of_number=number*factorial(number-1) # recursive case
        return factorial_of_number
print (factorial(4))