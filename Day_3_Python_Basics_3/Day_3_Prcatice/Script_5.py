# Script 5: The Pattern Printer (Nested Loops)
# Concept: Loops inside loops.
# 1. Ask the user for a number n (e.g., 5).
# 2. Write a loop that runs n times.
# 3. Inside that loop, print a star * multiplied by the current loop number.
# 4. Expected Output if n=5:

# Example Input: 5
# *
# **
# ***
# ****
# *****
input_number = input("Enter a number:")
n = int(input_number)
for i in range(1, n + 1):
    print('*' * i)