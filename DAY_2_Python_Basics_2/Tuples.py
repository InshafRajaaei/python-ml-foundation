# Tuples is like a list but it is immutable (can not be changed).
# once created, you cannot add, remove or modify items in a tuple.
# Syntax: Parentheses ()
# Used for data that should not change (Coordinates, RGB color values, Days of a week, etc.)

coordinates = (10, 20)
rgb_color = (255, 0, 0)

print(coordinates[0]) # Accessing items (Indexing)
# coordinates[0] = 15   This will raise an error because tuples are immutable

# Tuple Methods
# Tuples have only two built-in methods: count() and index()
print(coordinates.count(10)) # Counts how many times 10 appears in the tuple
print(coordinates.index(20)) # Returns the index of the first occurrence of 20
# You can convert a list to a tuple using the tuple() function
my_list = [1, 2, 3]
my_tuple = tuple(my_list)

print(my_tuple)
print(type(my_tuple)) # <class 'tuple'>
# You can also convert a tuple to a list using the list() function
converted_list = list(coordinates)
print(converted_list)
print(type(converted_list)) # <class 'list'>
# Looping through a tuple
for coord in coordinates:
    print(coord)
# Tuple Packing and Unpacking
point = (5, 10) # Packing
x, y = point   # Unpacking
print("X:", x)
print("Y:", y)
# Tuple Length
print(len(coordinates)) # Number of items in the tuple
# Nested Tuples
nested_tuple = ((1, 2), (3, 4), (5, 6))
print(nested_tuple[1][0]) # Accessing items in a nested tuple
# Single Item Tuple
single_item_tuple = (42,) # Note the comma
print(type(single_item_tuple)) # <class 'tuple'>
print(single_item_tuple[0])
# Without the comma, it would be just an integer
not_a_tuple = (42)
print(type(not_a_tuple)) # <class 'int'>
# Tuples are generally faster than lists for iteration and have a smaller memory footprint.
print("Iterating through coordinates tuple:")
for coord in coordinates:
    print(coord)
# Tuples can be used as keys in dictionaries because they are immutable.
my_dict = {coordinates: "This is a point"}
print(my_dict[coordinates])
# Tuples are often used to represent fixed collections of items, such as RGB color values or coordinates.
print("RGB Color:", rgb_color)
# They provide a way to group related data together in a single, immutable structure.
print("Coordinates:", coordinates)
# --- IGNORE ---
# End of recent edits
