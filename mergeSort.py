def merge_sort(list):
    if len(list)>1:
        #devide the array into 2 halves
        mid= len(list)/2
        leftArray = list[0:mid]
        leftArray = list[mid:len(list)]

numbers=[2,9,6,7,8,3,4]
merge_sort()
