# Create a set of prime numbers less than 50. Write a program to check whether a given number exists in the set or not.
prime_set = set()

for num in range(2, 50):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        prime_set.add(num)

print("Prime numbers less than 50:", prime_set)

check_num = int(input("Enter a number to check: "))

if check_num in prime_set:
    print(f"{check_num} is a prime number and exists in the set.")
else:
    print(f"{check_num} is not in the prime number set.")