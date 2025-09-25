
lista=[9,0,6,1,4,5]
lista.sort(reverse=True) # simple sort
print(lista)
list2=[]
students_new=[]
students = [('Alice', 85), ('Bob', 92), ('Charlie', 78)]
for student in students:
    name, score = student
    list2.append(score)
    print(f"Student: {name}, Score: {score}")       

list2.sort()
print("sorted list is ",list2)

students_new= sorted(students, key=lambda x: x[1]) # sort by score
print("sorted by score",students_new)