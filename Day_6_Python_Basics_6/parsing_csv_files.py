# A CSV (Comma seperated values) file is just a text file where data is seperated by commas.
# Mathod 1: Manual Parsing (The hard way) 
# Reading a CSV using standard string manipulation ( .split() , .strip() ).This is excellent for understanding how parsing works under the hood.)

with open("data.csv", "r") as f:
    header = f.readline()  # Skip the first line (Header)
    
    for line in f:
        clean_line = line.strip()      # Remove leading/trailing whitespace/newline
        row = clean_line.split(",")    # Split by commas into a list | row is now ['Bob', '22', 'Student']
        name = row[0]
        age = int(row[1])
        role = row[2]
        print(f"{name} is {age} years old and works as a {role}")

# Method 2: The csv Module (The easy way)
# Python has a built-in library that handles edge cases (like commas inside quotes).
import csv

with open("data.csv", "r") as f:
    reader =  csv.reader(f)
    next(reader) #Skip header row

    for row in reader:
        print(row) # row is ['Bob', '22', 'Student']