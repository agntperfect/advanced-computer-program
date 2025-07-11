#Question 5: Write a Python function that accepts a list and returns a new list containing only the elements at even indexes and those that are prime numbers. [cite: 12]
l = [2,3,4,5,6,7,8,9]
even_indices = range(0,len(l),2)
print(even_indices)


for index in even_indices:
    count = 0
    for i in range(1,l[index]+1):
        if (l[index]%i==0):
            count +=1
    if count==2:
        print(l[index])


def get_even_indexed_and_prime_elements(input_list):
    new_list = []
    # Add elements at even indexes
    for i in range(0, len(input_list), 2):
        new_list.append(input_list[i])

    # Add prime numbers
    for num in input_list:
        if num <= 1:
            continue
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime and num not in new_list: # Avoid duplicates if a prime is also at an even index
            new_list.append(num)
    return new_list

# Example usage of the new code:
my_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
result = get_even_indexed_and_prime_elements(my_list)
print(f"Elements at even indexes and prime numbers: {result}")