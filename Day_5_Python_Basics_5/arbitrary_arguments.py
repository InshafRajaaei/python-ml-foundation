# Arbitrary Arguments (*args)
# Allow a function to accept any number of positional arguments. Python collect them into a Touple.
# Syntax: Add a * before the parameter name

def sum_all(*numbers):
    total = 0
    for i in numbers:
        total +=i
    return total

print(sum_all(1, 2, 3, 4, 5)) #15
print(sum_all(10, 49 ,23)) #82

# Arbitrary Keyword Argumnets (**kwargs)
# Allow a function to accept any number of keyword argumnets.
# Python collects them into a dictionary.
# Syntax: Add ** before the parameter name

def print_info(**info):
    # info is dictionary : {'name': 'Bob' , 'age': 30}
    for key, value in info.items():
        print(f"{key}:{value}")

print_info(name="bob", age=30, school="XYZ High school")