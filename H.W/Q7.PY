# Q7
numbers = []
n = int(input("How many numbers: "))

for i in range(n):
    num = int(input("Enter number: "))
    
    if num > 1:
        prime = True
        for j in range(2, num):
            if num % j == 0:
                prime = False
                break
        
        if prime:
            numbers.append(num)

prime_tuple = tuple(numbers)

print("Prime numbers tuple:", prime_tuple)
