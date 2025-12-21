# Script 2: The FizzBuzz Challenge (Classic Interview Q)
# Concept: Complex Conditionals (if/elif/else order matters).

# 1. Loop through numbers from 1 to 20.
# 2. For each number:
#   - If divisible by 3 and 5: Print "FizzBuzz".
#   - If divisible by 3 (only): Print "Fizz".
#   - If divisible by 5 (only): Print "Buzz".
#   - Otherwise: Print the number itself.

# Hint: The order of your if statements is critical!

for num in range(1, 21):
    if num % 3 == 0 and num % 5 ==0:
        print("fizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)