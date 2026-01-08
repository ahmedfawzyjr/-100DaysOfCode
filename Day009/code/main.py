# Day 009: Sets

# Creating sets
print("=== Creating Sets ===")
fruits = {"apple", "banana", "cherry"}
numbers = {1, 2, 3, 4, 5}
mixed = {1, "hello", 3.14, True}
print(f"Fruits: {fruits}")
print(f"Numbers: {numbers}")

# Removing duplicates
print("\n=== Removing Duplicates ===")
numbers_with_dupes = [1, 2, 2, 3, 3, 3, 4, 5, 5]
unique_numbers = set(numbers_with_dupes)
print(f"Original: {numbers_with_dupes}")
print(f"Unique: {unique_numbers}")

# Adding and removing
print("\n=== Adding and Removing ===")
colors = {"red", "green"}
colors.add("blue")
print(f"After add: {colors}")
colors.remove("green")
print(f"After remove: {colors}")
colors.discard("yellow")  # Won't raise error if not found
print(f"After discard: {colors}")

# Set operations
print("\n=== Set Operations ===")
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union = set1 | set2  # or set1.union(set2)
print(f"Union: {union}")

intersection = set1 & set2  # or set1.intersection(set2)
print(f"Intersection: {intersection}")

difference = set1 - set2  # or set1.difference(set2)
print(f"Difference (set1 - set2): {difference}")

symmetric_diff = set1 ^ set2  # or set1.symmetric_difference(set2)
print(f"Symmetric Difference: {symmetric_diff}")

# Subset and superset
print("\n=== Subset and Superset ===")
set_a = {1, 2, 3}
set_b = {1, 2, 3, 4, 5}
print(f"set_a is subset of set_b: {set_a.issubset(set_b)}")
print(f"set_b is superset of set_a: {set_b.issuperset(set_a)}")

# Membership testing
print("\n=== Membership Testing ===")
vowels = {"a", "e", "i", "o", "u"}
print(f"'a' in vowels: {'a' in vowels}")
print(f"'b' in vowels: {'b' in vowels}")

# Set comprehension
print("\n=== Set Comprehension ===")
squares = {x**2 for x in range(1, 6)}
print(f"Squares: {squares}")

# Frozen set (immutable)
print("\n=== Frozen Set ===")
frozen = frozenset([1, 2, 3, 4, 5])
print(f"Frozen set: {frozen}")
# frozen.add(6)  # This would raise an error

# Practical example: Finding common friends
print("\n=== Common Friends Example ===")
alice_friends = {"Bob", "Carol", "Dave"}
bob_friends = {"Alice", "Carol", "Eve"}
common = alice_friends & bob_friends
print(f"Common friends: {common}")

# Length and clearing
print("\n=== Other Operations ===")
sample = {1, 2, 3, 4, 5}
print(f"Length: {len(sample)}")
sample.clear()
print(f"After clear: {sample}")
