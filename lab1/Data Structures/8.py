# Given a list of names, write a program to count how many times each name appears using a dictionary.
names = ["Alice", "Bob", "Alice", "Eve", "Bob", "Alice"]

count_dict = {}

for name in names:
    if name in count_dict:
        count_dict[name] += 1
    else:
        count_dict[name] = 1

print("Name counts:", count_dict)