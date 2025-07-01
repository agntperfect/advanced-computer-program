names = ["Alice", "Bob", "Alice", "Eve", "Bob", "Alice"]

count_dict = {}

for name in names:
    if name in count_dict:
        count_dict[name] += 1
    else:
        count_dict[name] = 1

print("Name counts:", count_dict)