# There is a difference between the print() and return.
# - print() displays the output to the console.
# - return sends the result back to the caller and can be stored in a variable or used in expressions.
# Function with PRINT (Displays but returns None)
def add_print(a, b):
    print(a + b)

# Function with RETURN (Gives value back)
def add_return(a, b):
    return a + b

# Usage:
x = add_print(5, 5)   # x is None. You cannot use the result.
y = add_return(5, 5)  # y is 10.
z = y * 2             # z is 20. (We can do math because we have the data!)
print(z)