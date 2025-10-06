students=[]
i=1
for i in range(6):
    students.append(int((input("enter student "+str(i)+ " marks: "))))
students.sort()
print(students)