# Q.No.6: Write a program to create a tuple of n numbers, then find:
# a. The average of the numbers
# b. The median
# c. The mode (without using libraries)

def input_tuple():
    n = int(input("Enter the number of elements: "))
    print("Enter the numbers:")
    nums = []
    for _ in range(n):
        nums.append(int(input()))
    return tuple(nums)

def calculate_average(t):
    total = 0
    for num in t:
        total += num
    return total / len(t)

def find_median(t):
    sorted_list = list(t)
    for i in range(len(sorted_list)):
        for j in range(len(sorted_list) - i - 1):
            if sorted_list[j] > sorted_list[j + 1]:
                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
    n = len(sorted_list)
    if n % 2 == 0:
        return (sorted_list[n // 2 - 1] + sorted_list[n // 2]) / 2
    else:
        return sorted_list[n // 2]

def find_mode(t):
    unique = []
    counts = []
    for num in t:
        if num in unique:
            index = unique.index(num)
            counts[index] += 1
        else:
            unique.append(num)
            counts.append(1)
    max_freq = counts[0]
    mode_val = unique[0]
    for i in range(1, len(counts)):
        if counts[i] > max_freq:
            max_freq = counts[i]
            mode_val = unique[i]
    return mode_val

def main():
    t = input_tuple()
    print("Tuple:", t)
    print("Average:", calculate_average(t))
    print("Median:", find_median(t))
    print("Mode:", find_mode(t))

main()