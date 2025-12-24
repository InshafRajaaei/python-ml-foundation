# the open() function
# Python uses the built-in open() function to interact with files.
# It requires two main arguments: The file path and the Mode.
# Syntax: file_object = open("filename.txt", "mode")

# file modes: Must tell Python what you intend to do with the file.

# Mode, Name,   Description,    Pointer Position
# 'r',  Read,   Default. Opens for reading. Errors if file doesn't exist.,                          Beginning
# 'w',  Write,  Opens for writing. Creates file if missing. Overwrites (deletes) existing content., Beginning
# 'a',  Append, Opens for writing. Creates file if missing. Adds to the end.,                       End
# 'x',  Create, Creates a specific file. Returns an error if the file already exists.,              Beginning

# The with statement (Context Manager)
# Best practice: Never use open() and close() manually. If your code crashes before close(), the file stays locked or corrupted.
# Use the with keyword. It automatically closes the file even if an error occurs.

# The wrong way (risky)
# import os
# print(os.getcwd())

# f = open("data.txt", "r")
# content = f.read()
# f.close()

# The right way (safe)
with open("data.txt", "r") as file:
    content = file.read()

#file.read()  # This will raise an error because the file is already closed.
    # Files closes automatically
# Python opens data.txt in read-only mode
# No changes to the file
# File pointer is at the start of the file

# Python reads ALL text from the file
# Stores it in the variable content as a string
# The file content is now in RAM

# content = "the text inside data.txt"
print(content)