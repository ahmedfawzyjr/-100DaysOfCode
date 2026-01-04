# Day 005: While Loops

# Basic while loop
print("=== Basic While Loop ===")
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1

# Countdown timer
print("\n=== Countdown Timer ===")
countdown = 5
while countdown > 0:
    print(f"{countdown}...")
    countdown -= 1
print("Blast off!")

# Sum until condition
print("\n=== Sum Until Condition ===")
total = 0
num = 1
while total < 50:
    total += num
    num += 1
print(f"Sum reached {total} after adding {num-1} numbers")

# User input validation
print("\n=== Input Validation ===")
# Simulating user input validation
attempts = 0
max_attempts = 3
password = "secret"
user_input = ""

while user_input != password and attempts < max_attempts:
    attempts += 1
    print(f"Attempt {attempts}: Enter password")
    # In real scenario: user_input = input("Password: ")
    user_input = "wrong" if attempts < 3 else "secret"
    
if user_input == password:
    print("Access granted!")
else:
    print("Access denied. Too many attempts.")

# Break statement
print("\n=== Using Break ===")
counter = 0
while True:
    counter += 1
    if counter > 5:
        break
    print(f"Counter: {counter}")

# Continue statement
print("\n=== Using Continue ===")
num = 0
while num < 10:
    num += 1
    if num % 2 == 0:
        continue  # Skip even numbers
    print(f"Odd number: {num}")

# While-else
print("\n=== While-Else ===")
n = 0
while n < 3:
    print(f"n = {n}")
    n += 1
else:
    print("Loop completed normally")
