# Script 2: The Student Database (List of Dicts)
# Concept: Looping through nested data.
# 1. Create this list:
# students = [
#     {"name": "Alice", "score": 85},
#     {"name": "Bob", "score": 62},
#     {"name": "Charlie", "score": 45},
#     {"name": "Diana", "score": 91}
# ]
# 2. Loop through the list.
# 3. For each student, check their score:
# If score >= 50, print: [Name] passed.
# If score < 50, print: [Name] failed.
students = [
    {"name" : "Alice","score" : 85},
    {"name" : "Bob", "score" : 62},
    {"name": "Charlie", "score": 45},
    {"name": "Diana", "score": 91}
]
print([students])
for stu in students:
    if stu["score"] >= 50:
        print(f"{stu['name']} passes.")
    else:
        print(f"{stu['name']} failed.")
