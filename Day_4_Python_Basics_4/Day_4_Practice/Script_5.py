# Script 5: The Prime Number Checker
# Concept: Logic & Break.

# 1. Ask the user for a number num.
# 2. If num is less than 2, print "Not Prime".
# 3. Else, create a boolean flag is_prime = True.
# 4. Loop from 2 to num (exclusive).
#   Check if num % i == 0 (divisible).
#   If yes: Set is_prime = False and break.
# 5. After the loop, check the flag. If is_prime is True, print "Prime". Else, print "Not Prime".

num = int(input("Enter a number:"))
if num < 2:
    print("not Prime")
else:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print("Prime")
    else:
        print("not Prime")