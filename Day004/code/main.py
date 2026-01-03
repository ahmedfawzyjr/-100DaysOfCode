# Day 004: For Loops

# Basic for loop
print("=== Basic For Loop ===")
for i in range(5):
    print(f"Iteration {i}")

# Iterating over a list
print("\n=== Iterating Over List ===")
fruits = ["apple", "banana", "cherry", "date"]
for fruit in fruits:
    print(f"I like {fruit}")

# Iterating over a string
print("\n=== Iterating Over String ===")
word = "Python"
for char in word:
    print(char, end=" ")
print()

# Using range with start, stop, step
print("\n=== Range with Parameters ===")
for num in range(2, 11, 2):
    print(f"Even number: {num}")

# Sum of numbers
print("\n=== Sum Calculator ===")
total = 0
for i in range(1, 11):
    total += i
print(f"Sum of 1 to 10: {total}")

# Multiplication table
print("\n=== Multiplication Table (5) ===")
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")

# Nested loops - Pattern printing
print("\n=== Pattern Printing ===")
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()

# Using enumerate
print("\n=== Using Enumerate ===")
colors = ["red", "green", "blue"]
for index, color in enumerate(colors, start=1):
    print(f"{index}. {color}")

# Break and continue
print("\n=== Break and Continue ===")
for num in range(1, 11):
    if num == 5:
        continue  # Skip 5
    if num == 8:
        break  # Stop at 8
    print(num, end=" ")
print()
