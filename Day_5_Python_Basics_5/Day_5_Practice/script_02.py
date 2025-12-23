# Script 2: The Even/Odd Checker (Boolean Return)
# Goal: Returning Logic.

# 1. Define a function is_even(number).
# 2. If the number is even (number % 2 == 0), return True.
# 3. Else, return False.
# 4. Write a main loop that asks the user for a number and uses your function to print "Even" or "Odd".

def is_even(number):
    return number % 2 == 0
    # even = False
    # if number % 2 == 0:
    #     even = True
    # return even
count = 0
while count < 10:
    ipt = int(input("Enter a number: "))
    res = is_even(ipt)
    print("Even" if is_even(ipt) else "Odd")
    count += 1
    # if res: # if res == True: (basic)
    #     print("Even")
    # else:
    #     print("Odd")
