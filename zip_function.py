#zip
list1=[1,2,3]
list2=['a','b','c']
zipp_object=zip (list1, list2)
print(type(zipp_object))
print(zipp_object)
#print(list(zipp_object))
print(dict(zipp_object))

dict1={'a':1,'b':2,'c':3}
list3=[3,4,5]
zipp_object2=zip (dict1.keys(), list3)
print(list(zipp_object2))

print("------------")
print(zipp_object2)
###unzip
listOfZipObject=list(zipp_object2)
print(listOfZipObject)
unzipped_object=zip(*listOfZipObject)

print(unzipped_object)

lista, listb = list(unzipped_object)
print(lista)
print(listb)

zipped = [(1, 'a'), (2, 'b'), (3, 'c')]
unzipped = zip(*zipped)
list1, list2 = list(unzipped)
print(list1) # (1, 2, 3)
print(list2) # ('a', 'b', 'c')

