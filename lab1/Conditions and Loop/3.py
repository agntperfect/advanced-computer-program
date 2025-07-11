# Write a program that reads a number and prints the factorial of that number using a while loop.
n = int(input("Enter a number: "))
factorial = 1
i = 1

while i <= n:
    factorial *= i
    i += 1

print(f"Factorial of {n} is {factorial}")