# Q no. 11:
# Given a list of numbers with duplicates, use a set to remove the duplicates.
# Then, convert it back to a sorted list and display the result.

def remove_duplicates_and_sort(numbers):
    unique_numbers = set(numbers)        
    sorted_numbers = sorted(unique_numbers)  
    return sorted_numbers
numbers = [5, 3, 8, 3, 9, 1, 5, 7, 8, 2]
result = remove_duplicates_and_sort(numbers)
print(result)