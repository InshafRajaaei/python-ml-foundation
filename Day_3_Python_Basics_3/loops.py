# loops allow to iterate over data structures to process items individually.

# 1. For Loop
# The for loop iterates over a sequence (list, tuple, dictionary, string) and executes a block of code for each item.
# Syntax
# | for variable_name in sequance:
    # | code block to be executed

# looping ranges
# the range(start, stop, step) function generates a sequence of numbers.
# range(5) -> 0, 1, 2, 3, 4 (stop value is exclusive)
# range(1, 4) -> 1, 2, 3
# range(0, 10, 2) -> 0, 2, 4, 6, 8 (2 step value)

# looping through lists
colors = ["red", "green", "blue"]
for color in colors:
    print("Current color: {color}".format(color=color))

# Looping through Dictionaries
# By default, iterating a dictionary gives you the keys
person = {"name": "Alice", "age": 30, "city": "New York", "job":"Dev"}

# 1. Loop Keys (Default)
for key in person:
    print(key)

# 2. Loop Values
for val in person.values():
    print(val)

# 3. Loop Both (Items) - Most Common
for key, val in person.items():
    print(f"{key}: {val}")

# Loop control keywords
# break : Immediately exit the loop
# continue : Skip the current iteration and move to the next one