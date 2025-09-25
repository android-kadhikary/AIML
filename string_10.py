str="enter the string:"
splited_string_in_list=str.split()
print("str = ",str)
print("word in the string = ",splited_string_in_list)
l1=[]
i=len(splited_string_in_list)-1
while i>=0:
    l1.append(splited_string_in_list[i])
    i=i-1
print(l1)    
output =' '.join(l1)
print(output)



def revstr(st):
    return st[ : :-1]
print(revstr(("learning the python is easy")))