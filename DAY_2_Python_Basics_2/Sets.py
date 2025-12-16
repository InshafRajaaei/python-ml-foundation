# Set is unorderd and allows no duplicate elements
# syntax to create a set: Curly Braces {}
# Things that don't change (Unique items, Tags, Categories)

my_set = {1, 2, 3, 4, 5, 5, 5}
print(my_set) # Output: {1, 2, 3, 4, 5} (duplicates are removed)

# Key Operations
# Adding Items
my_set.add(6) # Adds 6 to the set
print(my_set)

# Removing Items
my_set.remove(3) # Removes 3 from the set, raises KeyError if not
print(my_set)

my_set.discard(10) # Removes 10 if present, does nothing if not
print(my_set)
popped_item = my_set.pop() # Removes and returns an arbitrary item
print("Popped item:", popped_item)
print(my_set)

# Set Length
print(len(my_set)) # Number of items in the set

# Looping through a set
for item in my_set:
    print(item)
# Checking if an item exists
if 4 in my_set:
    print("4 is in the set!")
# Set Operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}
# Union
set_union = set_a.union(set_b)
print("Union:", set_union) # {1, 2, 3, 4
# Intersection
set_intersection = set_a.intersection(set_b)
print("Intersection:", set_intersection) # {3}
# Difference
set_difference = set_a.difference(set_b)
print("Difference (A - B):", set_difference) # {1, 2}
# Symmetric Difference
set_sym_diff = set_a.symmetric_difference(set_b)
print("Symmetric Difference:", set_sym_diff) # {1, 2, 4, 5}
# Subset and Superset
print("Is A subset of B?", set_a.issubset(set_b)) # False
print("Is A superset of B?", set_a.issuperset(set_b)) # False
# Frozen Set - Immutable version of a set
frozen_set = frozenset([1, 2, 3, 4])
print("Frozen Set:", frozen_set)
# --- IGNORE ---
# End of recent edits

