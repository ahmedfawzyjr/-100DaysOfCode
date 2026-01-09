# Day 010: Functions - Basics

# Simple function
def greet():
    """Simple greeting function"""
    print("Hello, World!")

print("=== Simple Function ===")
greet()

# Function with parameters
def greet_person(name):
    """Greet a person by name"""
    print(f"Hello, {name}!")

print("\n=== Function with Parameters ===")
greet_person("Alice")
greet_person("Bob")

# Function with return value
def add(a, b):
    """Add two numbers and return the result"""
    return a + b

print("\n=== Function with Return ===")
result = add(5, 3)
print(f"5 + 3 = {result}")

# Multiple parameters
def calculate_area(length, width):
    """Calculate rectangle area"""
    area = length * width
    return area

print("\n=== Multiple Parameters ===")
area = calculate_area(10, 5)
print(f"Area: {area}")

# Multiple return values
def get_min_max(numbers):
    """Return both minimum and maximum from a list"""
    return min(numbers), max(numbers)

print("\n=== Multiple Return Values ===")
nums = [3, 7, 2, 9, 1, 5]
minimum, maximum = get_min_max(nums)
print(f"Min: {minimum}, Max: {maximum}")

# Function with no return (returns None)
def print_info(name, age):
    """Print person information"""
    print(f"Name: {name}, Age: {age}")

print("\n=== Function with No Return ===")
result = print_info("Charlie", 25)
print(f"Return value: {result}")

# Docstring example
def calculate_bmi(weight, height):
    """
    Calculate Body Mass Index (BMI)
    
    Parameters:
    weight (float): Weight in kilograms
    height (float): Height in meters
    
    Returns:
    float: BMI value
    """
    bmi = weight / (height ** 2)
    return round(bmi, 2)

print("\n=== BMI Calculator ===")
bmi = calculate_bmi(70, 1.75)
print(f"BMI: {bmi}")
print(f"\nDocstring: {calculate_bmi.__doc__}")

# Function calling other functions
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5/9

def convert_temperature(value, to_unit):
    """Convert temperature between C and F"""
    if to_unit == 'F':
        return celsius_to_fahrenheit(value)
    elif to_unit == 'C':
        return fahrenheit_to_celsius(value)
    else:
        return None

print("\n=== Temperature Converter ===")
print(f"25°C = {convert_temperature(25, 'F')}°F")
print(f"77°F = {convert_temperature(77, 'C')}°C")

# Boolean return functions
def is_even(number):
    """Check if number is even"""
    return number % 2 == 0

def is_prime(n):
    """Check if number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print("\n=== Boolean Functions ===")
print(f"Is 4 even? {is_even(4)}")
print(f"Is 7 prime? {is_prime(7)}")
print(f"Is 10 prime? {is_prime(10)}")
