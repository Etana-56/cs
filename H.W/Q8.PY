# Q8
employees = []

n = int(input("Enter number of employees: "))

for i in range(n):
    name = input("Enter employee name: ")
    employees.append(name)

employees.sort()

print("Sorted employee names:")
for name in employees:
    print(name)
