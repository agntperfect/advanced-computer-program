# Given two lists, write a program to find their intersection using sets.
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]
intersection = list(set(list1) & set(list2))
print("Intersection:", intersection)