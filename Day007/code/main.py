# Day 007: Tuples

# Creating tuples
print("=== Creating Tuples ===")
coordinates = (10, 20)
colors = ("red", "green", "blue")
single = (42,)  # Note the comma for single element
empty = ()
print(f"Coordinates: {coordinates}")
print(f"Colors: {colors}")
print(f"Single element: {single}")

# Tuple packing and unpacking
print("\n=== Packing and Unpacking ===")
person = "Alice", 25, "Engineer"  # Packing
name, age, job = person  # Unpacking
print(f"Name: {name}, Age: {age}, Job: {job}")

# Accessing elements
print("\n=== Accessing Elements ===")
point = (5, 10, 15)
print(f"X: {point[0]}, Y: {point[1]}, Z: {point[2]}")
print(f"Last element: {point[-1]}")

# Tuple methods
print("\n=== Tuple Methods ===")
numbers = (1, 2, 3, 2, 4, 2, 5)
print(f"Count of 2: {numbers.count(2)}")
print(f"Index of 3: {numbers.index(3)}")
print(f"Length: {len(numbers)}")

# Tuple slicing
print("\n=== Tuple Slicing ===")
data = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(f"First 5: {data[:5]}")
print(f"Last 3: {data[-3:]}")
print(f"Every 2nd: {data[::2]}")

# Nested tuples
print("\n=== Nested Tuples ===")
matrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print(f"Matrix: {matrix}")
print(f"Element [1][2]: {matrix[1][2]}")

# Tuple operations
print("\n=== Tuple Operations ===")
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined = tuple1 + tuple2
print(f"Combined: {combined}")
repeated = tuple1 * 3
print(f"Repeated: {repeated}")

# Immutability demonstration
print("\n=== Immutability ===")
try:
    coordinates[0] = 100  # This will raise an error
except TypeError as e:
    print(f"Error: {e}")
print("Tuples cannot be modified!")

# Converting between list and tuple
print("\n=== List ↔ Tuple Conversion ===")
my_list = [1, 2, 3, 4, 5]
my_tuple = tuple(my_list)
print(f"List to Tuple: {my_tuple}")
back_to_list = list(my_tuple)
print(f"Tuple to List: {back_to_list}")
