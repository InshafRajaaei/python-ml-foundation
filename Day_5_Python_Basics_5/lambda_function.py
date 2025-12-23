# A lambda function is a small, one-line function that has no name. 
# It is often used for short, simple operations or inside other functions(like sorting).
# Can take many argumnets but have only one expression.

# Stabdard function
def add(a, b):
    return a + b

# Lambda function
add_l = lambda a, b: a + b

print(add(5, 10)) # Using standard function
print(add_l(5, 10)) # Using lambda function

# Real-world example: Sorting a list of dictionaries by a specific key using lambda function
students = [
    {"name": "Alice", "score": 90},
    {"name": "Bob", "score": 85},
    {"name": "Charlie", "score": 75}
]
# Sort students by score using lambda function
sorted_students = sorted(students, key=lambda x: x["score"])
print(sorted_students)
# sorted() | Built-in Python function | Returns a new sorted list | Does not change the original students list.
# key=lambda x: x["score"] | key tells Python what to sort by | lambda x: x["score"] means: | Take one element (x) from the list | Extract its "score" value | Use that value for comparison
# “Sort the students based on their score.”

# lambda x: x["score"]
# Actually
# def get_score(x):
    # return x["score"]

# students.sort(key=lambda x: x["score"])
# What this line does | students.sort() sorts the existing list in place | It modifies students directly | It returns None (this matters) | After this line runs, students itself is sorted by score.

# Before
# [
#     {"name": "Alice", "score": 90},
#     {"name": "Bob", "score": 85},
#     {"name": "Charlie", "score": 75}
# ]

# After
# [
#     {"name": "Charlie", "score": 75},
#     {"name": "Bob", "score": 85},
#     {"name": "Alice", "score": 90}
# ]

# When you SHOULD use .sort()
# You don’t need the original order
# You want better performance (slightly faster, no extra list)
# You’re okay with mutating the list

# When you should NOT
# You need the original list unchanged
# You’re working with shared data (side effects matter)
students.sort(key=lambda x: x["score"], reverse=True)
print(students)