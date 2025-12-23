# Functions become powerful when they can accept data.
# Parameter - The variable listed inside the parantheses in the function definition(the placeholder).
# Argument - The actual value sent to the function when it is called (the data).

# 1. Positional Arguments - The arguments match the order of the parameters.
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")

introduce("Alice", 28)

# 2. Keyword Arguments - Can specify which parameter assigning, ignoring the order.
introduce(age=40, name="Bob")

# 3. default Parameters - Parameters can have default values. Can provide a default value if the user doesn,t pass one.
def make_coffee(coffee_type="Espresso"):
    print(f"Making a cup of {coffee_type} coffee.")

make_coffee("Latte")
make_coffee()