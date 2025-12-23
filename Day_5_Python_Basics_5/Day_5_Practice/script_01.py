# Script 1: The Area Calculator (Basic)
# Goal: Practice Parameters and Return.

# 1. Define a function calculate_area(length, width).
# 2. Inside, calculate area = length * width.
# 3. Return the area.
# 4. Outside the function:
#  -Ask the user for length and width.
#  -Call the function and store the result in a variable.
#  -Print: "The area is [Result]".

def calculate_area(length, width):
    area = length * width
    return area

input_length = float(input("Enter Length: "))
input_width = float(input("Enter width: "))
area_cal = calculate_area(input_length, input_width)
print("The area is", area_cal)