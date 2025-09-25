def sum_all(list1,*args):
    print (list1)
    print(args[0], args[2])
    return sum(args)
#print(sum_all(['a','b'],1, 2, 3)) # Output: 6
#print(sum_all([5, 10], 15,9,6))


def display_info(title,classname,**kwargs):
    for key, value in kwargs.items():
        print(classname, "  ", title)
        print(f"{key}: {value}")
#display_info(title="Python",name="Alice", age=25, city="New York",classname="func")
# Output:
# name: Alice
# age: 25
# city: New York

# def referance_type(set_type):
#     return set_type
# set_set={5,2,9,6,7,2,3,2}
# s2={10,11}
# print(type(set_set), " && ",id(set_set))
# set_set={5,2,9,6,7}
# print(set_set)
# print(type(set_set), " && ",id(set_set))

# tup_set=(5,2,9,6,7,2,3,2)
# print(type(tup_set), " && ",id(tup_set))
# tup_set=tup_set*2
# print(tup_set)
# print(type(tup_set), " && ",id(tup_set))
#referance_type(set_set)

def referance_type(set_type):
    return set_type
list_set=[5,2,9,6,7,2,3,2]
list1=list_set
print(type(list_set), " && ",id(list_set))
print(type(list1), " && ",id(list1))
list_set=[5,2,9,6,7]
print(list_set)
print(list1)
print(type(list_set), " && ",id(list_set))
print(type(list1), " && ",id(list1))