# Day 002: Python Operators

# Arithmetic Operators
a, b = 15, 4
print("=== Arithmetic Operators ===")
print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")
print(f"Floor Division: {a} // {b} = {a // b}")
print(f"Modulus: {a} % {b} = {a % b}")
print(f"Exponentiation: {a} ** 2 = {a ** 2}")

# Comparison Operators
print("\n=== Comparison Operators ===")
x, y = 10, 20
print(f"{x} == {y}: {x == y}")
print(f"{x} != {y}: {x != y}")
print(f"{x} < {y}: {x < y}")
print(f"{x} > {y}: {x > y}")
print(f"{x} <= {y}: {x <= y}")
print(f"{x} >= {y}: {x >= y}")

# Logical Operators
print("\n=== Logical Operators ===")
is_sunny = True
is_warm = False
print(f"Sunny AND Warm: {is_sunny and is_warm}")
print(f"Sunny OR Warm: {is_sunny or is_warm}")
print(f"NOT Sunny: {not is_sunny}")

# Assignment Operators
print("\n=== Assignment Operators ===")
num = 10
print(f"Initial value: {num}")
num += 5
print(f"After += 5: {num}")
num *= 2
print(f"After *= 2: {num}")
num //= 3
print(f"After //= 3: {num}")
