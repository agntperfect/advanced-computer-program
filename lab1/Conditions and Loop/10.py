# Write a menu-driven program to perform arithmetic operations (+, -, *, /) based on user choice using conditional statements.
print("Select Operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter choice (1/2/3/4): ")

# Input two numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

# Perform operation based on choice
if choice == '1':
    print(f"{a} + {b} = {a + b}")
elif choice == '2':
    print(f"{a} - {b} = {a - b}")
elif choice == '3':
    print(f"{a} * {b} = {a * b}")
elif choice == '4':
    if b != 0:
        print(f"{a} / {b} = {a / b}")
    else:
        print("Error: Division by zero.")
else:
    print("Invalid choice.")