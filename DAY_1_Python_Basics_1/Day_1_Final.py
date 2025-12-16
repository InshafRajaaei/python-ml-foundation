x = 10 % 4
result = x + 3
print(type(result)) #int

y = 5.0
z = y * 2
print(type(z)) #float

user_age = "20"
user_age_num = int(user_age)
result2 = user_age_num + 5
print(type(result2)) #int

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

# The bug is here!
# total = num1 + num2
total = int(num1) + int(num2)

print("The sum is:", total)