# Script 3: The Right-Angled Triangle (Nested Loops)
# Concept: Visual Patterns.

# 1. Ask the user for the height of the triangle n (e.g., 5).
# 2. Write a loop for i in range(1, n + 1).
# 3. Inside, print "*" multiplied by i.

# *
# **
# ***
# ****

num = int(input("Enter the height of the triangle:"))
for i in range(1, num + 1):
    print("*" * i)