# List is the most common tool.
# It is ordered and changable.
# Can put anything and you can add/remove wherever you want.
# Syntax: Square Bracket []
# Things that change (Shopping lists, To-Do lists, Player scores).

# A list of strings
fruits = ["Apple", "Banana", "Cherry"]

# A list can hold mixed items
random_stuff = ["Inshaf", 100, 5.5, True]

# Key Operations

# Accessing items (Indexing) Counts from 0
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[-1]) # Last item (Negative numbers count from the end)

# Adding Items
fruits.append("Orange") # Adds to the end
fruits.insert(1, "Grape") # Adds at a specific index
print(fruits)

# Removing Items
fruits.remove("Banana") # Removes the first Banana it finds
del fruits[0] # Removes item at index 0
fruits.pop(1) # Removes the item at index 1 and returns it
print(fruits)

# List Length
print(len(fruits)) # Number of items in the list

# Looping through a list
for fruit in fruits:
    print(fruit)
# Checking if an item exists
if "Cherry" in fruits:
    print("Cherry is in the list!")
# Modifying an item
fruits[0] = "Mango" # Change the first item to Mango
print(fruits)
# List Slicing
print(fruits[0:2]) # Items from index 0 to 1 (2 is excluded)
print(fruits[:2])  # Items from start to index 1
print(fruits[1:])  # Items from index 1 to the end

# List Methods

fruits.sort() # Sorts the list alphabetically
print(fruits)

fruits.reverse() # Reverses the list
print(fruits)

fruits.clear() # Empties the list
print(fruits)

# You can also use list() to create a list from another iterable
numbers = list(range(5)) # Creates a list [0, 1, 2, 3, 4]
print(numbers)

# End of DAY_2_Python_Basics_2/Lists.py