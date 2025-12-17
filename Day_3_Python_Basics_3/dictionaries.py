# A dictionary is a python in build data structure which used to store data in key value pairs.
# Lists are indexed by the range of numbers but Dictionaries are indexed by keys.
# - Mapping Type : Key-Value Pairs
# - Mutable : Can be changed
# - Ordered : As of Python 3.7, dictionaries maintain insertion order
# - No duplicate keys allowed

# Syntax and Creation
# Curly Braces {}

# Empty Dictionary
empty_dict = {}

# Standard Dictionary
user_profile = {
    "username": "InshafRMNaazir",
    "id": 5261,
    "is_admin": True,
    "skills": ["Python", "Verilog", "Web Development"]
}

# Rules
# - Keys : Must be immutable data types (Strings, Integers, Floats, Tuples). Can not use a List as a key because lists can change.
# - Values : Can be aby data type (Strings, Lists, Other Dictionaries, Boolean, etc...)

# CRUD Operations

# Accessing Values (read)
# Can access the values be referencing the key inside square brackets [].
print(user_profile["username"])
# the .get() method(best practice) can also be used to access values. 
# If we try to acces a key that npt exist using [] Puthon will throw a KeyError, to avoid crashing, use .get() method. It return None if the key is missing.
print(user_profile.get("email"))
role = user_profile.get("role", "Guest")

# Adding and updating
# If the key exists, the value is updated
# If the key does not exist, a new key pair created
user_profile["location"] = "Maruthamunai" # Creates new key
user_profile["id"] = 2022

# Deleting
# Method 1: del keyword
del user_profile["is_admin"]
# Method 2: pop() method
removed_id = user_profile.pop("id")

# Essential Dictionary Methods
# keys() - returns a view object containing all the keys in the dictionary
keys = user_profile.keys()
print(keys)
# values() - returns a view object containing all the values in the dictionary
values = user_profile.values()
print(values)
# items() - returns a view object containing all the key-value pairs in the dictionary as tuples
items = user_profile.items()
print(items)
# update() - updates the dictionary with key-value pairs from another dictionary or iterable of key-value pairs
additional_info = {
    "email": "inshaf.rm.naazir@gmail.com"
}
user_profile.update(additional_info)
print(user_profile)
# clear() - removes all key-value pairs from the dictionary
user_profile.clear()
print(user_profile)  # Output: {}