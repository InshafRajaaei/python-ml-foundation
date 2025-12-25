# Script 1: The Logger (Append Mode)
# Goal: Keep a persistent log of user actions.

# Ask the user: "Enter a log message:".
# Open a file named log.txt in Append mode ("a").
# Write the message + a newline character (\n) to the file.
# Run the script 3 times with different messages.
# Open log.txt manually to check if all 3 messages are there.

input_msg =  input("Enter a log message : ")
with open("log.txt", "a", encoding="utf-8") as file:
    file.write(f"{input_msg}\n")