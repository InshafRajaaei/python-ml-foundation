# Script 4: The Inverted Pyramid
# Concept: Decrementing logic.

# 1. Ask for height n.
# 2. Write a loop that goes backwards.
#   - Hint: range(n, 0, -1)
# 3. Print stars inside the loop.

# *****
# ****
# ***
# **
# *

num = int(input("Enter the height of the inverted pyramid:"))
for i in range(num, 0, -1):
    print("*" * i)
