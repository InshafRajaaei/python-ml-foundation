# Script 3: The Frequency Counter
# Concept: Logic and Dictionary building.
# Create a long string: text = "python is great and python is easy".

# 1. Split the string into a list of words using .split() (Google this method if needed).
# 2. Create an empty dictionary word_counts = {}.
# 3. Loop through the list of words:
#   If the word is not in word_counts, add it with value 1.
#   If the word is in word_counts, increment its value by 1.
# 4. Print the dictionary. (Result should show how many times each word appeared).

text = "python is great and python is easy"
split = text.split()
print(split)
word_count = {}
for wrd in split:
    if wrd not in word_count:
        word_count[wrd] = 1
    else:
        word_count[wrd] += 1
print(word_count)