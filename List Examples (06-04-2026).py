# find maximum and minimum number in a list
numbers = [3, 5, 1, 9, 2]
max_num = max(numbers)
min_num = min(numbers)
print("Maximum number:", max_num)
print("Minimum number:", min_num)

# Reverse a list
numbers = [3, 5, 1, 9, 2]
numbers.reverse()
print("Reversed list:", numbers)

# remove Duplicates from a list
numbers = [3, 5, 1, 9, 2, 3, 5]
unique_numbers = list(set(numbers))
print("Unique numbers:", unique_numbers)

# find second largest element in a list
numbers = [3, 5, 1, 9, 2]
numbers.sort(reverse=True)
print("Second largest number:", numbers[1])

# Merge two sorted lists
list1 = [1, 3, 5]
list2 = [2, 4, 6]
marged_list = sorted(list1 + list2)
print("Merged sorted list:", marged_list)


# check for symmetrical list
def is_symmetrical(lst):
    return lst == lst[::-1]


symmetrical_list = [1, 2, 3, 2, 1]
print("Is the list symmetrical?", is_symmetrical(symmetrical_list))
