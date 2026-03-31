# Q1: Count vowels in a string
text = input("Enter a string: ")
count = 0

for char in text.lower():
    if char in "aeiou":
        count += 1

print("Number of vowels:", count)


# Q2: Find the largest number in a set using for loop
numbers = {10, 25, 7, 99, 45}
largest = None

for num in numbers:
    if largest is None or num > largest:
        largest = num

print("Largest number is:", largest)


# Q3: Pyramid pattern
for i in range(1, 6):
    print("*" * i)


# Q4: Remove duplicates from a list using for loop
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = []

for item in my_list:
    if item not in unique_list:
        unique_list.append(item)

print("List without duplicates:", unique_list)


# Q5: Multiplication table generator
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)


# Q6: Find common elements in two lists using for loop and zip()
list1 = [1, 2, 3, 4]
list2 = [3, 2, 5, 4]
common = []

for a, b in zip(list1, list2):
    if a == b:
        common.append(a)

print("Common elements:", common)


# Q7: Password validation
password = input("Enter password: ")

if (len(password) >= 8 and
    any(c.isupper() for c in password) and
    any(c.islower() for c in password) and
    any(c.isdigit() for c in password)):
    print("Valid password")
else:
    print("Invalid password")


# Q8: Function prints Good Morning
def morning():
    print("Good Morning!")

morning()


# Q9: Function takes user's name and prints greeting
def greet(name):
    print("Hello,", name)

greet("Ahmed")


# Q10: Function takes two numbers and prints sum
def add(a, b):
    print("Sum =", a + b)

add(5, 7)


# Q11: Function returns area of rectangle
def rectangle_area(length, width):
    return length * width

print("Area =", rectangle_area(5, 4))


# Q12: Function prints largest number in list
def largest_number(lst):
    print("Largest number:", max(lst))

largest_number([5, 8, 2, 10, 3])


# Q13: Function returns reverse string
def reverse_string(text):
    return text[::-1]

print(reverse_string("python"))


# Q14: Function returns factorial
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(5))


# Q15: Username and password validation
def check_login(username, password):
    if username == "admin" and password == "1234":
        return "Valid"
    else:
        return "Invalid"

username = input("Enter username: ")
password = input("Enter password: ")

print(check_login(username, password))


# Q16: Guess the random number game
import random

def guess_game():
    number = random.randint(1, 100)

    while True:
        guess = int(input("Guess the number: "))

        if guess > number:
            print("Too high")
        elif guess < number:
            print("Too low")
        else:
            print("Correct!")
            break

guess_game()