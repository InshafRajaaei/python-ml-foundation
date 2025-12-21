# Script 1: The Secure Login (While Loop)
# Concept: Keeping the user trapped until they satisfy a condition.

# 1. Define a correct password variable (e.g., "secret123").
# 2. Use a while True loop (an infinite loop structure).
# 3. Inside the loop, ask the user: "Enter password:".
# Check:
#   - If the input matches the password: Print "Access Granted" and break.
#   - If not: Print "Try again".

correct_password = "secret123"
while True:
    user_input = input("Enter password:")
    if user_input == correct_password:
        print("Access Granted")
        break
    else:
        print("Try again")