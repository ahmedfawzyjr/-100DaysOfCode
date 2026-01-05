# Day 006: Python Lists

# Creating lists
print("=== Creating Lists ===")
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]
mixed = [1, "hello", 3.14, True]
print(f"Numbers: {numbers}")
print(f"Fruits: {fruits}")
print(f"Mixed: {mixed}")

# Accessing elements
print("\n=== Accessing Elements ===")
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")
print(f"Second fruit: {fruits[1]}")

# List slicing
print("\n=== List Slicing ===")
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"First 5: {nums[:5]}")
print(f"Last 5: {nums[-5:]}")
print(f"Every 2nd: {nums[::2]}")
print(f"Reversed: {nums[::-1]}")

# List methods
print("\n=== List Methods ===")
shopping = ["milk", "bread"]
shopping.append("eggs")
print(f"After append: {shopping}")
shopping.insert(1, "butter")
print(f"After insert: {shopping}")
shopping.remove("bread")
print(f"After remove: {shopping}")
last_item = shopping.pop()
print(f"Popped: {last_item}, List: {shopping}")

# List operations
print("\n=== List Operations ===")
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(f"Combined: {combined}")
repeated = list1 * 3
print(f"Repeated: {repeated}")
print(f"Length: {len(combined)}")
print(f"Max: {max(combined)}, Min: {min(combined)}")

# List comprehension
print("\n=== List Comprehension ===")
squares = [x**2 for x in range(1, 6)]
print(f"Squares: {squares}")
evens = [x for x in range(1, 11) if x % 2 == 0]
print(f"Evens: {evens}")

# Sorting
print("\n=== Sorting ===")
unsorted = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_list = sorted(unsorted)
print(f"Sorted (new list): {sorted_list}")
unsorted.sort(reverse=True)
print(f"Sorted in place (desc): {unsorted}")
