# Write a program to input key-value pairs from the user and store them in a dictionary. Allow the user to search for a key and display its value.

data = {}

print("Enter key-value pairs (type 'stop' as key to end):")

while True:
    key = input("Enter key: ")
    if key.lower() == 'stop':
        break
    value = input("Enter value: ")
    data[key] = value

search_key = input("Enter a key to search: ")

if search_key in data:
    print(f"Value for '{search_key}': {data[search_key]}")
else:
    print(f"Key '{search_key}' not found.")