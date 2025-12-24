# Handling errors (try / except)
# Files often fail (file missing, permission denied). Must handle this things.
try:
    with open("missing_file.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
        print("Error: The file was not found.")
except PermissionError:
        print("Error: You do not have permission to access this file.")

# File Paths (os vs pathlib)
# Windows uses backslashes \. Linux/Mac use forward slashes /. Hardcoding paths causes bugs.
from pathlib import Path

# Creates a path that works on ANY operating system
folder = Path("documents")
file_path = folder / "datacreate.txt" 

if file_path.exists():
    print("File found!")

from pathlib import Path
import os

print("=== WHERE PYTHON IS RUNNING FROM ===")
print("Current Working Directory:")
print(os.getcwd()) #C:\xxxxxx\python-ml-foundation
print()

# 1. Create a Path object for a folder
folder = Path("documents") # This does NOT create the folder on disk yet
print("Folder Path object:", folder) #documents
print("Does folder exist?", folder.exists()) #False because not created yet
print() # empty line

# 2. Create a Path object for a file INSIDE that folder
file_path = folder / "data.txt" # Still does NOT create anything on disk
print("File Path object:", file_path) #documents/data.txt
print("Does file exist?", file_path.exists()) #False because not created yet
print() # empty line

# 3. Actually create the folder (if missing)
folder.mkdir(exist_ok=True) # exist_ok=True prevents error if folder already exists. This will create only the folder, not the file.
print("Folder created (or already existed)") #documents
print("Does folder exist now?", folder.exists()) #True because we just created it
print() # empty line

# 4. Write text to the file
file_path.write_text("Hello!\nThis file was created using pathlib.") # This creates the file and writes text to it
print("File written.") #documents/data.txt
print() # empty line

# 5. Read the file back
content = file_path.read_text() # Reads the entire file content as a string
print("=== FILE CONTENT ===") 
print(content) # Hello!\nThis file was created using pathlib.

# 6. Show path details
print("=== PATH DETAILS ===") # Path object has many useful properties
print("File name:", file_path.name) # data.txt
print("Parent folder:", file_path.parent) # documents
print("Absolute path:", file_path.resolve()) # Full path from root
