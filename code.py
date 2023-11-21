# Variable example
x = 10
y = 5
z = x + y

print(z)  # Output: 15

# Function example
def add(x, y):
    return x + y

# String formatting example
name = "Alice"
age = 25

# Using f-string
message = f"My name is {name} and I am {age} years old."
print(message)  # Output: My name is Alice and I am 25 years old.

# Using format() method
message = "My name is {} and I am {} years old.".format(name, age)
print(message)  # Output: My name is Alice and I am 25 years old.

# Using positional arguments
message = "My name is {0} and I am {1} years old.".format(name, age)
print(message)  # Output: My name is Alice and I am 25 years old.

# Using named arguments
message = "My name is {name} and I am {age} years old.".format(name=name, age=age)
print(message)  # Output: My name is Alice and I am 25 years old.

# Using format specifiers
pi = 3.14159
formatted_pi = "{:.2f}".format(pi)
print(formatted_pi)  # Output: 3.14

# Getting user input example
name = input("Enter your name: ")
print(f"Hello {name}!")  # Output: Hello Alice!

# Lists, tuples, and sets example
# Lists
numbers = [1, 2, 3, 4, 5]
print(numbers)  # Output: [1, 2, 3, 4, 5]
# Tuples
numbers = (1, 2, 3, 4, 5)
print(numbers)  # Output: (1, 2, 3, 4, 5)
# Sets
numbers = {1, 2, 3, 4, 5}
print(numbers)  # Output: {1, 2, 3, 4, 5}
# Dictionaries
student = {
    "name": "John",
    "age": 20,
    "major": "Computer Science"
}
print(student)  # Output: {'name': 'John', 'age': 20, 'major': 'Computer Science'}

# Advanced set operation example
# Union
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)  # Output: {1, 2, 3, 4, 5}
# Intersection
a = {1, 2, 3}
b = {3, 4, 5}
print(a & b)  # Output: {3}
# Difference
a = {1, 2, 3}
b = {3, 4, 5}
print(a - b)  # Output: {1, 2}
# Symmetric difference
a = {1, 2, 3}
b = {3, 4, 5}
print(a ^ b)  # Output: {1, 2, 4, 5}

#Boolean example
x = 10
y = 5
print(x > y)  # Output: True
print(x < y)  # Output: False
print(x == y)  # Output: False
print(x != y)  # Output: True
print(x >= y)  # Output: True
print(x <= y)  # Output: False

# If-else example
x = 10
y = 5
if x > y:
    print("x is greater than y")   # Output: x is greater than y
else:
    print("x is less than or equal to y")   # This line is not executed

# If-elif-else example
x = 10
y = 5
if x > y:
    print("x is greater than y")   # Output: x is greater than y
elif x < y:
    print("x is less than y")   # This line is not executed
else:
    print("x is equal to y")

# The in keyword example
numbers = [1, 2, 3, 4, 5]
print(1 in numbers)  # Output: True
print(6 in numbers)  # Output: False

# Loop example
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)

# Original code
numbers = [1, 2, 3, 4, 5]

# List comprehension
squared_numbers = [num ** 2 for num in numbers]

print(squared_numbers)

# Output: [1, 4, 9, 16, 25]

# Destructuring variables
name, age, major = student.values()

print(name)  # Output: John
print(age)  # Output: 20
print(major)  # Output: Computer Science



