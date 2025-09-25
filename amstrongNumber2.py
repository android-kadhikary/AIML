#print (1%10)

def is_amstrong_number(number):
    power = len(str(number))
    result= 0
    while (number%10)!=0:
        print (number%10)
        result = result + pow((number%10), power)
        print ("res1", result)
        number=number//10
        print("Num1 ", number)
    
    if(result == number):
        print("amstrong", result , number)
    else:
        print("amstrong", result , number)
    return result    
number=153
result = is_amstrong_number(number)
print("result", result , number)
