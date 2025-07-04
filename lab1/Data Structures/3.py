# Write a Python function that accepts a list and returns a new list with only the even numbers from the original list.
sample_list = list(range(1, 10))
even = [num for num in sample_list if num % 2 == 0]
print("Original list:", sample_list)
print("Even numbers:", even)