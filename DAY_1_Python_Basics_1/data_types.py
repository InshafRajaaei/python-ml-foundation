# Data types tells what kind of value a variable holds.
# The data type determines what operation can be performed on that variable.
# Python is dynamically typed, meaning we don't need to declare the type it will figured out automatically.

# Common Data Types in Python:

# 1. Numeric Types:
# 1.1 Integer int - whole numbers, positive or negative without decimals
# Example: 10, -500, 0
# 1.2 Float float - Numbers with decimal points(floating point numbers)
# Example: 10.5, -3.14, 0.001

# 2. Text Type:
# 2.1 String str - A sequence of charcters enclosed in single (''), or double ("") qoutes.
# Example: "Hello, World!", '123345'

# 3. Boolean Type:
# 3.1 Boolean bool - Represents one of two values: True or False Used heavily in logic and conditions
# Example: True, False

# Use the built in type() function to confirm the data type of a varible
height = 160.5
is_studying = False

print(type(height))       #Output: <class 'float'>
print(type(is_studying))  #Output: <class 'bool'>
