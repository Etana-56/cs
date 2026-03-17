# Q1
stdmarks = []

n = int(input("How many students? "))

for i in range(n):
    name = input("Enter student name: ")
    mark = int(input("Enter student mark: "))
    stdmarks.append([name, mark])

new_name = input("Enter new student name: ")
new_mark = int(input("Enter new student mark: "))
stdmarks.insert(2, [new_name, new_mark])

new_name2 = input("Enter new name for the third student: ")
stdmarks[2][0] = new_name2

passedStudents = []

for student in stdmarks:
    if student[1] >= 50:
        passedStudents.append(student)

print("Passed students:")
for student in passedStudents:
    print(student[0], student[1])
