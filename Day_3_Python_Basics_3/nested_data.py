# Real world applications (API Databases JSON) rerey use flat data. They use nested structures.

# 1. List of Dictionaries (This is the standard format database records)
students = [
    {"id":1, "name":"alice", "gpa":3.8},
    {"id":2, "name":"bob", "gpa":3.5},
    {"id":3, "name":"charlie", "gpa":3.9}
]
# How to access "bob"
# 1. Select the list item (index 1)
# 2. Select the dictionary key "name"
print(students[1]["name"])

# 2. Dictionary of Lists
#useful for categorizing data
library = {
    "scific": ["Dune", "Neuromancer", "Foundation"],
    "fantasy": ["Harry Potter", "The Hobbit", "The Name of the Wind"]
}
# How to access "Dune"
print(library["scific"][0])

# 3. Deep Nesting (Combination of both)
data = {
    "status": "success",
    "user": {
        "id": 101,
        "preferences": {
            "theme": "dark",
            "notifications": ["email", "sms"]
        }
    }
}
# How to access "sms"
print(data["user"]["preferences"]["notifications"][1])