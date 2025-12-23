Self-Study Questions (Interview Prep)

1. Terminology: What is the difference between a function definition and a function call?

2. Logic: What does a function return if you don't write a return statement? (Answer: None).

3. Syntax: Can a function return two values? (Answer: Yes, Python returns them as a tuple).

def get_coords():
    return 10, 20  # Returns (10, 20)

4. Scope: If I have a global variable named x and a local variable named x inside a function, does changing the local one change the global one? (Answer: No, the local one "shadows" the global one).

5. Design: Why is it considered bad practice to use print() inside a function that performs a calculation? (Answer: It reduces reusability; you can't use the result for further math).