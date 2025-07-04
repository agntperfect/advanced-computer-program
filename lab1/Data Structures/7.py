# Write a Python program to merge two dictionaries and sum the values of common keys.
dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 15, 'c': 5, 'd': 40}

merged = dict1.copy() 

for key, value in dict2.items():
    if key in merged:
        merged[key] += value 
    else:
        merged[key] = value

print("Merged dictionary:", merged)