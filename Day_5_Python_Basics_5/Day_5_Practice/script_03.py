# Script 3: The Temperature Converter (Helper Functions)
# Goal: Calling functions inside functions.

# 1. Define celsius_to_fahrenheit(c) which returns the converted value ($F = C \times 1.8 + 32$).
# 2. Define fahrenheit_to_celsius(f) which returns the converted value ($C = (F - 32) / 1.8$).
# 3. Ask the user: "Type 1 for C->F, Type 2 for F->C".
# 4. Based on input, call the correct function and print the result.

def celsius_to_fahrenheit(c):
    return (c*1.8) + 32
def fahrenheit_to_celsius(f):
    return (f - 32) / 1.8

ipt = int(input("Type 1 for C->F, Type 2 for F->C: "))
if ipt == 1:
    ipt_temp = float(input("Enter the Temperature: "))
    print(celsius_to_fahrenheit(ipt_temp))
elif ipt ==2:
    ipt_temp = float(input("Enter the Temperature: "))
    print(fahrenheit_to_celsius(ipt_temp))
else:
    print("Invalid Choice")