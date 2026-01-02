# Day 003: Conditional Statements

# Simple if statement
age = 18
if age >= 18:
    print("You are an adult!")

# if-else statement
temperature = 25
if temperature > 30:
    print("It's hot outside!")
else:
    print("The weather is pleasant.")

# if-elif-else statement
score = 85
print("\n=== Grade Calculator ===")
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'
print(f"Score: {score}, Grade: {grade}")

# Nested conditionals
print("\n=== Login System ===")
username = "admin"
password = "pass123"

if username == "admin":
    if password == "pass123":
        print("Login successful!")
    else:
        print("Incorrect password")
else:
    print("Username not found")

# Ternary operator
print("\n=== Ternary Operator ===")
num = 15
result = "Even" if num % 2 == 0 else "Odd"
print(f"{num} is {result}")

# Multiple conditions
print("\n=== Eligibility Check ===")
age = 20
has_license = True

if age >= 18 and has_license:
    print("You can drive!")
elif age >= 18 and not has_license:
    print("You need a license to drive")
else:
    print("You're too young to drive")
