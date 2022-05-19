from functools import reduce

# Method-1

my_list = [[1], [2, 3], [4, 5, 6, 7]]
lst = []

for item in my_list:
    lst.extend(item)

print(lst)

# Method-2

flattened_list = [num for sublist in my_list for num in sublist]

print(flattened_list)

# Method-3

print(reduce(lambda x, y: x + y, my_list))
