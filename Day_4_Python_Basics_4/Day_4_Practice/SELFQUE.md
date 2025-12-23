Self-Study Questions
1. Logic: Why does if x % 3 == 0 and x % 5 == 0: have to come before if x % 3 == 0: in the FizzBuzz problem?

2. Scope: If I declare a variable count = 0 inside a for loop, what happens to it in every iteration? (Answer: It resets to 0 every time).

3. Syntax: What is the difference between = (assignment) and == (comparison)?

4. Infinite Loops: Why is while True: useful if it creates an infinite loop? (Hint: Used with break for "do-while" logic).

5. Output Prediction:

Python

x = 0
while x < 3:
    x += 1
    if x == 2:
        continue
    print(x)
(Answer: Prints 1, then skips 2, then prints 3).