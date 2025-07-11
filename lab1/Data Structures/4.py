# Write a program to count the number of each character in a given string using a dictionary.
input_string = "Hello World!"

char_count = {}  

for char in input_string:
    char_count[char] = input_string.count(char)

print("Character counts:")
for char, count in char_count.items():
    print(f"'{char}': {count}")