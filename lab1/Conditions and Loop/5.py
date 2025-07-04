# Write a program to find the largest and smallest number in a list entered by the user.
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

largest = max(numbers)
smallest = min(numbers)
print(numbers)
print(f"Largest number: {largest}")
print(f"Smallest number: {smallest}")