# Write a program to generate the Fibonacci sequence up to n terms.

n = int(input("Enter the number of terms: "))
print("nth term:", n)
a, b = 0, 1
print("Fibonacci sequence:")

for _ in range(n):
    print(a, end=' ')
    a, b = b, a + b