# Day 011: Advanced Functions

# Default parameters
def greet(name, greeting="Hello"):
    """Greet with custom or default greeting"""
    return f"{greeting}, {name}!"

print("=== Default Parameters ===")
print(greet("Alice"))
print(greet("Bob", "Hi"))
print(greet("Charlie", greeting="Hey"))

# *args - Variable positional arguments
def sum_all(*args):
    """Sum all provided numbers"""
    return sum(args)

print("\n=== *args Example ===")
print(f"Sum: {sum_all(1, 2, 3)}")
print(f"Sum: {sum_all(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}")

def print_info(*args):
    """Print all arguments"""
    for i, arg in enumerate(args, 1):
        print(f"Argument {i}: {arg}")

print("\n=== Multiple Args ===")
print_info("Python", 3.11, True, [1, 2, 3])

# **kwargs - Variable keyword arguments
def create_profile(**kwargs):
    """Create user profile from keyword arguments"""
    profile = {}
    for key, value in kwargs.items():
        profile[key] = value
    return profile

print("\n=== **kwargs Example ===")
user = create_profile(name="Alice", age=25, city="NYC", job="Engineer")
print(f"Profile: {user}")

# Combining *args and **kwargs
def flexible_function(*args, **kwargs):
    """Function accepting any arguments"""
    print(f"Positional args: {args}")
    print(f"Keyword args: {kwargs}")

print("\n=== Combined *args and **kwargs ===")
flexible_function(1, 2, 3, name="Bob", age=30)

# Lambda functions
print("\n=== Lambda Functions ===")
square = lambda x: x ** 2
add = lambda x, y: x + y
is_even = lambda x: x % 2 == 0

print(f"Square of 5: {square(5)}")
print(f"Add 3 and 7: {add(3, 7)}")
print(f"Is 4 even? {is_even(4)}")

# Lambda with map, filter, reduce
print("\n=== Lambda with Built-ins ===")
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Squared: {squared}")
print(f"Evens: {evens}")

# Sorting with lambda
print("\n=== Sorting with Lambda ===")
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78}
]
sorted_students = sorted(students, key=lambda x: x["grade"], reverse=True)
for student in sorted_students:
    print(f"{student['name']}: {student['grade']}")

# Function scope
global_var = "I'm global"

def outer_function():
    """Demonstrate scope"""
    outer_var = "I'm in outer"
    
    def inner_function():
        inner_var = "I'm in inner"
        print(f"Inner can see: {global_var}, {outer_var}, {inner_var}")
    
    inner_function()
    print(f"Outer can see: {global_var}, {outer_var}")

print("\n=== Function Scope ===")
outer_function()

# Closure example
def multiplier(n):
    """Return a function that multiplies by n"""
    def multiply(x):
        return x * n
    return multiply

print("\n=== Closure Example ===")
times_3 = multiplier(3)
times_5 = multiplier(5)
print(f"3 * 10 = {times_3(10)}")
print(f"5 * 10 = {times_5(10)}")
