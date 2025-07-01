# Write a program that finds all numbers between 100 and 999 where the sum of the cubes of the digits equals the number itself (Armstrong numbers).

print("Armstrong numbers between 100 and 999:")

for num in range(100, 1000):
    digits = [int(d) for d in str(num)]
    cube_sum = sum(d ** 3 for d in digits)
    
    if cube_sum == num:
        print(num)