# 1. Reading Methods
# .read() - Reads the entire file into a single string.
# with open("notes.txt", "r") as f:
#     data = f.read()

# print(data)
# .readline() - Reads a single line from the file.
with open("notes.txt", "r") as f:
    first_line = f.readline()
    second_line = f.readline()
print(first_line)
print(second_line)

# .readlines() - Reads all lines into a list of strings.
with open("notes.txt", "r") as f:
    lines = f.readlines()

print(lines) # List of lines = ['line1\n', 'line2\n', 'line3\n']

# 2. Writing Methods
# .write(string): Write astring to the file
# .writelines(list): Write a list of strings to the file.
# Writing using .write()
with open("output.txt", "w") as f:
    f.write("Hello, World!\n")
    f.write("This is a new line.\n")
print("Data written using .write()")

lines = ["First Line\n", "Second Line\n", "Third Line\n"]
with open("output_lines.txt", "w") as f:
    f.writelines(lines)