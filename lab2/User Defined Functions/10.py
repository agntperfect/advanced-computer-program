# Q no. 10:
# Write a Python function that accepts a sentence and returns a set of all unique vowels used.

def unique_vowels(sentence):
    vowels = set("aeiouAEIOU")
    return {char.lower() for char in sentence if char in vowels}

sentence = "Innovation distinguishes between a leader and a follower."
print(unique_vowels(sentence))