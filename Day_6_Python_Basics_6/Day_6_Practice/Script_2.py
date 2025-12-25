# Script 2: The File copier
# Goal: Read from one, write to another.

# Create a file source.txt with some random text.
# Write a script that opens source.txt in Read mode.
# Read the content.
# Open backup.txt in Write mode.
# Write the content into backup.txt.
# Print "Backup successful!"

with open("source.txt", "r") as file:
    content = file.readlines()
print(content)
with open("backup.txt","w",encoding="utf-8") as f:
    f.write(f"{content}")
    print("Backup Successful")