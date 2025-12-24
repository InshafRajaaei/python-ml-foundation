# If you handle non-English characters (or english), might get wired symbols.
# Always force UTF-8
# with open("data.txt", "r", encoding="utf-8") as f:
#     pass

# with open("data.txt", "r") as file: #rise error because the data contain the sinhala and emoji in that file
#     content = file.readlines()

with open("data.txt", "r", encoding="utf-8") as file:
    content = file.readlines()
print(content)