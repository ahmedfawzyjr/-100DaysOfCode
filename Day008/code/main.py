# Day 008: Dictionaries

# Creating dictionaries
print("=== Creating Dictionaries ===")
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A",
    "courses": ["Math", "Physics"]
}
print(f"Student: {student}")

# Accessing values
print("\n=== Accessing Values ===")
print(f"Name: {student['name']}")
print(f"Age: {student.get('age')}")
print(f"GPA: {student.get('gpa', 'Not found')}")  # Default value

# Adding and modifying
print("\n=== Adding and Modifying ===")
student["email"] = "alice@email.com"
student["age"] = 21
print(f"Updated student: {student}")

# Dictionary methods
print("\n=== Dictionary Methods ===")
print(f"Keys: {list(student.keys())}")
print(f"Values: {list(student.values())}")
print(f"Items: {list(student.items())}")

# Iterating through dictionary
print("\n=== Iterating ===")
for key, value in student.items():
    print(f"{key}: {value}")

# Removing items
print("\n=== Removing Items ===")
removed = student.pop("email")
print(f"Removed: {removed}")
print(f"After removal: {student}")

# Nested dictionaries
print("\n=== Nested Dictionaries ===")
classroom = {
    "student1": {"name": "Bob", "grade": 85},
    "student2": {"name": "Carol", "grade": 92},
    "student3": {"name": "Dave", "grade": 78}
}
print(f"Bob's grade: {classroom['student1']['grade']}")

# Dictionary comprehension
print("\n=== Dictionary Comprehension ===")
squares = {x: x**2 for x in range(1, 6)}
print(f"Squares: {squares}")

# Merging dictionaries
print("\n=== Merging Dictionaries ===")
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = {**dict1, **dict2}
print(f"Merged: {merged}")

# Word frequency counter
print("\n=== Word Frequency Counter ===")
text = "hello world hello python world"
words = text.split()
frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1
print(f"Frequency: {frequency}")

# Checking existence
print("\n=== Checking Keys ===")
print(f"'name' in student: {'name' in student}")
print(f"'phone' in student: {'phone' in student}")
