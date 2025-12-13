# This allows the program to communicate with user

# Output: priny() - function displys information to the user's console
message = "Good Day!"
print(message)  # Output: Good Day!

# Printing multiple items
name = "Inshaf"
age = 23
print("Hello,",name,"you are", age, "years old.")

# Input: input() - function pauses the program and waits for the user to type something and press the enter
# The Golden Rule of input(): It always the data as a srtring
user_input = input("Please enter your city: ")
print("You live in", user_input)
print(type(user_input))  # Output: <class 'str'>
