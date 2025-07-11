# Q.No.1: Write a program to input n numbers and store them in a list. Then perform the following operations:
# i) Find max, min, sorted list, and remove duplicates using built-in functions.
# ii) Perform the same operations without using any built-in functions.

def input_numbers():
    n = int(input("Enter the number of elements: "))
    numbers = []
    print("Enter the numbers:")
    for _ in range(n):
        numbers.append(int(input()))
    return numbers

# Using built-in functions
def using_builtins(numbers):
    print("\n--- Using Built-in Functions ---")
    print("Maximum:", max(numbers))
    print("Minimum:", min(numbers))
    print("Sorted List:", sorted(numbers))
    print("List without duplicates:", list(set(numbers)))

# Without using built-in functions
def find_max_min(numbers):
    max_num = numbers[0]
    min_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
    return max_num, min_num

def bubble_sort(numbers):
    sorted_list = numbers[:]
    for i in range(len(sorted_list)):
        for j in range(0, len(sorted_list) - i - 1):
            if sorted_list[j] > sorted_list[j + 1]:
                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
    return sorted_list

def remove_duplicates(numbers):
    unique_list = []
    for num in numbers:
        if num not in unique_list:
            unique_list.append(num)
    return unique_list

def without_builtins(numbers):
    print("\n--- Without Using Built-in Functions ---")
    max_val, min_val = find_max_min(numbers)
    print("Maximum:", max_val)
    print("Minimum:", min_val)
    print("Sorted List:", bubble_sort(numbers))
    print("List without duplicates:", remove_duplicates(numbers))

def main():
    numbers = input_numbers()
    print("\nOriginal List:", numbers)
    using_builtins(numbers)
    without_builtins(numbers)

main()