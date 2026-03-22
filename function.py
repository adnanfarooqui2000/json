# =========================== Functions in Python ===============================================
# Block of code that can be called multiple times

# Global variable example
y = 10

def add(x):
    global y  # Use global keyword to modify global variable
    y = 20
    sum = x + y
    print("Inside function:", sum)

print("Before function:", y)  # Output: 10
add(10)  # Output: Inside function: 30
print("After function:", y)   # Output: 20

# Alternative using globals()
y = 10
def add_using_globals(x):
    sum = x + globals()['y']  # Access global variable without modifying it
    print("Using globals():", sum)

add_using_globals(10)  # Output: Using globals(): 20
print("y remains:", y)  # Output: y remains: 10

# Types of functions (1. Built-in functions, 2. User-defined functions)

# User-defined function syntax
def add(x, y):
    z = x + y
    return z

# Function call
result = add(10, 20)
print("Addition result:", result)  # Output: 30

# Function with user input
def get_input_and_add():
    p = int(input("Enter First Digit: "))
    q = int(input("Enter Second Digit: "))
    return add(p, q)

# result = get_input_and_add()
# print("User input result:", result)
# Function with default parameters
def plus(a=0, b=0):
    c = a + b
    return c

# Different ways to call
print(plus())        # Output: 0
print(plus(5))       # Output: 5
print(plus(5, 10))   # Output: 15

# Square function
def square(x):
    return x * x

z = int(input("Enter any digit: "))
print("Square of", z, "is:", square(z))

# *args for variable number of arguments
def add(*numbers):
    total = 0
    for i in numbers:
        total += i
    return total

print("Sum of 10, 20:", add(10, 20))  # Output: 30
print("Sum of 10-100:", add(10, 20, 30, 40, 50, 60, 70, 80, 90, 100))  # Output: 550

# **kwargs for keyword arguments
def emp_data(**data):
    for key, value in data.items():
        print(key, "=", value)

emp_data(Name="Adnan Farooqui", city="Bhopal", age=25)

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def multi(x, y):
    return x * y

def div(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def mode(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x % y

def power(x, y):
    return x ** y

def floor_div(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x // y

def calculator():
    operations = {
        1: ("Addition", add),
        2: ("Subtraction", sub),
        3: ("Multiplication", multi),
        4: ("Division", div),
        5: ("Modulus", mode),
        6: ("Power", power),
        7: ("Floor Division", floor_div)
    }
    
    while True:
        print("\n=== Calculator Menu ===")
        for key, (name, _) in operations.items():
            print(f"{key}. {name}")
        print("8. Exit")
        
        try:
            choice = int(input("Select operation (1-8): "))
            
            if choice == 8:
                print("Thank you for using the calculator!")
                break
                
            if choice not in operations:
                print("Invalid choice! Please select 1-8")
                continue
                
            p = float(input("Enter First Number: "))
            q = float(input("Enter Second Number: "))
            
            operation_name, operation_func = operations[choice]
            result = operation_func(p, q)
            print(f"{operation_name} of {p} and {q} = {result}")
            
        except ValueError:
            print("Please enter valid numbers!")
        except Exception as e:
            print(f"Error: {e}")

# Uncomment to run calculator
# calculator()

# Traditional approach
my_list = [10, 20, 30, 40, 50]
new_list = []
for i in my_list:
    x = i + 5
    new_list.append(x)
print("Traditional:", new_list)

# Map function syntax: map(function, iterable)
numbers = [5, 10, 15, 20, 25]

def check_even_odd(n):
    return 'Even' if n % 2 == 0 else 'Odd'

result = tuple(map(check_even_odd, numbers))
print("Map result:", result)

# Filter function
my_list = [10, 15, 20, 25, 30, 35, 40]

def is_even(n):
    return n % 2 == 0

even_numbers = tuple(filter(is_even, my_list))
print("Filter result:", even_numbers)

# Lambda functions (anonymous functions)
# Syntax: lambda arguments: expression

# Simple lambda
greet = lambda name: print("Hello", name)
greet("Adnan")

# Lambda with multiple parameters
add = lambda x, y: x + y
print("Lambda addition:", add(5, 3))

# Lambda with map
numbers = [2, 4, 6, 8, 10]
squares = list(map(lambda x: x**2, numbers))
print("Squares using lambda:", squares)

# Lambda with filter
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers using lambda:", even_numbers)

from functools import reduce

# Using reduce to find maximum
my_list = [1, 5, 98, 5, 85, 86, 7, 8]

def find_max(x, y):
    return x if x > y else y

max_value = reduce(find_max, my_list)
print("Maximum value:", max_value)

# Using lambda with reduce
max_value_lambda = reduce(lambda x, y: x if x > y else y, my_list)
print("Max with lambda:", max_value_lambda)

# Sum using reduce
total = reduce(lambda x, y: x + y, my_list)
print("Total sum:", total)

"""
Function vs Loop:

Functions are reusable and need to be called

Loops execute immediately but aren't reusable

Variable Scope:

Use global keyword to modify global variables

Use globals()['var_name'] to access without modifying

Function Types:

Built-in: int(), str(), sum(), etc.

User-defined: Created with def keyword

Best Practices:

Always validate user input

Handle division by zero errors

Use meaningful function names

Add comments for complex logic
"""