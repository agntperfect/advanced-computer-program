# Q no. 9:
# Create a set of random numbers. Add more numbers until the set has 10 unique elements.
# Also, remove the smallest and largest element.

import random

def create_and_modify_set(initial_numbers):
    numbers = set(initial_numbers)

    while len(numbers) < 10:
        numbers.add(random.randint(1, 100))

    numbers.remove(min(numbers))
    numbers.remove(max(numbers))
    
    return numbers

initial_set = {3, 7, 15}  
result_set = create_and_modify_set(initial_set)
print("Final set after additions and removals:", result_set)