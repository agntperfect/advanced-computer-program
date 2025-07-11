# Write a program that accepts 10 integers from the user and counts how many are positive, negative, and zero.

positive = 0
negative = 0
zero = 0

print("Enter 10 integers:")

for _ in range(10):
    num = int(input())
    print(num)
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    else:
        zero += 1

print(f"Positive numbers: {positive}")
print(f"Negative numbers: {negative}")
print(f"Zeros: {zero}")