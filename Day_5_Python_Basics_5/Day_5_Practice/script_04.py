# Script 4: The Vowel Counter (String Processing)
# Goal: Strings + Loops + Functions.

# 1. Define a function count_vowels(text).
# 2. Inside, define a list of vowels vowels = "aeiouAEIOU".
# 3. Set a counter to 0.
# 4. Loop through every character in text. If the character is in vowels, increment the counter.
# 5. Return the final count.
# 6. Test it with the input: "Python Programming is Amazing". (Should return 9).

def count_vowels(text):
    vowels = "aeiouAEIOU"
    counter = 0
    for ch in text:
        for chrr in vowels:
            if chrr == ch:
                counter += 1
    return counter

text = input("Enter the string to check the vowels : ")
print(count_vowels(text))