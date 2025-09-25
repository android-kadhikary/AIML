d=1
def if_amstrong_number(number):
 result=0
 power= len(str(number))
 for digit_of_number in str(number):
  result =pow(int(digit_of_number),power)+result

 if result==number:
  print(" is amstrong number")
 else:
  print(" is not amstrong number")

if_amstrong_number(153)  