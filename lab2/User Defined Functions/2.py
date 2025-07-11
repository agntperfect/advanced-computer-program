# Q.no.2 Given two lists of integers, write a program to merge them into a single list and then remove the elements that are common in both.
def get_list(prompt):
    return list(map(int, input(prompt).split()))

def find_common_elements(l1, l2):
    common = []
    for i in l1:
        if i in l2 and i not in common:
            common.append(i)
    return common

def remove_common_and_merge(l1, l2, common):
    merged = l1 + l2
    result = []
    for item in merged:
        if item not in common:
            result.append(item)
    return result

def main():
    list1 = get_list("Enter elements of List 1 separated by space: ")
    list2 = get_list("Enter elements of List 2 separated by space: ")
    common = find_common_elements(list1, list2)
    result = remove_common_and_merge(list1, list2, common)
    print("Merged list without common elements:", result)

main()