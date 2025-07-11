# Q no. 13:
# Write a program that reads a text and counts the frequency of each character
# (excluding spaces and special characters) using a dictionary.

def char_frequency(text):
    freq = {}
    for char in text:
        if char.isalpha():  # Consider only alphabetic characters
            char_lower = char.lower()
            freq[char_lower] = freq.get(char_lower, 0) + 1
    return freq

text = "Hello, World! Welcome to the coding world."
frequency = char_frequency(text)
print(frequency)