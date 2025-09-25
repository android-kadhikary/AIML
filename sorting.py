numbers = [10, 5, 0, 2, 9, 3, 8, 4, 7, 6]
def sort_numbers(list1):
    i=0
    j=0
    num_fix_for_fullList= list1[i]
    for number in list1:
        if number == num_fix_for_fullList:
            pass
        elif number <num_fix_for_fullList:
            list1[i]=number
        else:
            pass    

    print(list1)

sort_numbers(numbers)