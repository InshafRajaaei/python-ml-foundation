# 1. The if, elif, else structure
# python relies on indentation (whitesspace) to define blocks of code.
# if - The first block is checked first.
# elif(else if) - Checked only if previous contion were false. cn have multiple elif statements.
# else - The fallback. Runs all previous conditions were false.
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: D")

# 2. Logical Operators
# can combine multiple conditions using logical operators.
# Operator, Description,                                        Example
# and,      Returns True if both statements are true.,          if x > 5 and x < 10:
# or,       Returns True if at least one statement is true.,    if x < 5 or x > 10:
# not,      Reverses the result (True becomes False).,          if not is_raining:

# 3. truthy and falsy values
# In Puthon, values can be evalated as booleans if they aren't explicitly True or False.
# Falsy values: 0, 0.0, ""(empty string), [](empty list), None, False.
username = ""
if not username:
    print("Username is empty.")

