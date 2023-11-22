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

# Function example
def add(x, y):
    return x + y

# Lambda function example
add = lambda x, y: x + y

# Dictionary comprehension example
numbers = [1, 2, 3, 4, 5]
squared_numbers = {num: num ** 2 for num in numbers}
print(squared_numbers)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Unpacking example
numbers = [1, 2, 3, 4, 5]
x, y, *rest = numbers
print(x)  # Output: 1
print(y)  # Output: 2
print(rest)  # Output: [3, 4, 5]

# Unpacking keyword arguments example
def func(*args, **kwargs):
    print(args)
    print(kwargs)

# Object-oriented programming example
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}.")

# Magic methods example
class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Person({self.name})"

    def __repr__(self):
        return f"Person({self.name})"

    def __eq__(self, other):
        return self.name == other.name

    def __add__(self, other):
        return Person(self.name + other.name)
    
# Class method example vs static method example
class Person:
    def __init__(self, name):
        self.name = name

    @classmethod
    def create(cls, name):
        return cls(name)

    @staticmethod
    def create(name):
        return Person(name)

# Class inheritance example vs composition example
# Inheritance
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}.")

class Student(Person):
    def __init__(self, name, major):
        super().__init__(name)
        self.major = major

    def study(self):
        print(f"I am studying {self.major}.")

# Composition
class AnotherPerson:
    def __init__(self, name):
        self.person = Person(name)

    def greet(self):
        self.person.greet()

# Type hinting example
def add(x: int, y: int) -> int:
    return x + y

# Error handling example
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print("Division successful.")
finally:
    print("This is always executed.")


# File handling example
# Write to file
with open("data.txt", "w") as file:
    file.write("Hello, world!")

# Read from file
with open("data.txt", "r") as file:
    data = file.read()
    print(data)  # Output: Hello, world!

# Importing module example
# Path: demo-python/main.py
import code

print(code.add(1, 2))  # Output: 3

# Custom error example
class CustomError(Exception):
    pass
# Raise custom error
raise CustomError("This is a custom error.")

# First class function example
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def apply(func, x, y):
    return func(x, y)


print(apply(add, 1, 2))  # Output: 3
print(apply(subtract, 1, 2))  # Output: -1
print(apply(multiply, 1, 2))  # Output: 2

# Simple decorator example
def decorator(func):
    def wrapper():
        print("Before function.")
        func()
        print("After function.")
    return wrapper

# at sign (@) syntax
@decorator
def hello():
    print("Hello, world!")

hello()  # Output: Before function. Hello, world! After function.

# Functools wraps example
from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Before function.")
        func(*args, **kwargs)
        print("After function.")
    return wrapper

@decorator
def hello():
    print("Hello, world!")

print(hello.__name__)  # Output: hello

# Do not use mutable objects as default arguments
def add(x, y=[]):
    y.append(x)
    return y

print(add(1))  # Output: [1]
print(add(2))  # Output: [1, 2]
print(add(3))  # Output: [1, 2, 3]

# Use None as default argument instead
def add(x, y=None):
    if y is None:
        y = []
    y.append(x)
    return y

print(add(1))  # Output: [1]
print(add(2))  # Output: [2]
print(add(3))  # Output: [3]


