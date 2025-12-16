# 1. Arithmatic operators - Python uses standard mathematical operators
# Operator,Name,            Description,                                                    Example,        Result
#   +     ,Addition,        Sums two values.,                                               5 + 3,          8
#   -     ,Subtraction,     Difference between two values.,                                 10 - 4,         6
#   *     ,Multiplication,  Product of two values.,                                         2 * 6,          12
#   /     ,Division,        Divides and always returns a float.,                            10 / 2,         5.0
#   //    ,Floor Division,  Divides and returns the integer part (drops the remainder).,    10 // 3,        3
#   %     ,Modulus,         Returns the remainder of the division.,                         10 % 3,         1
#   **    ,Exponentiation,  Raises the first number to the power of the second.,            2 ** 4 (24),    16

# 2. Type Casting - Converting one data type to another data type
# The input() gives the string then it want to convet into int or float
# int() - Coverts a value (usually a string) into an integer
# float() - Coverts a value (usually a string) into a float
# str() - Coverts a value (usually a string) into an integer

age_text = input("how old are you?") # string input
age_number = int(age_text) # converting the string into integer
next_age = age_number + 1
print("Next year your age will be:",next_age)