import numpy as np


# Method-1


def split(list_a, chunk_size):

    for i in range(0, len(list_a), chunk_size):
        yield list_a[i:i + chunk_size]


chunk_size = 2
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(split(my_list, chunk_size)))

# Method-2


def split(list_a, chunk_size):

    for i in range(0, len(list_a), chunk_size):
        print(list_a[i:i + chunk_size], end=" ")


chunk_size = 2
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
split(my_list, chunk_size)
print('\r')

# Method-3

chunk_size = 2
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

list_chunked = [my_list[i:i+chunk_size]
                for i in range(0, len(my_list), chunk_size)]

print(list_chunked)

# Method-4

list_chunked = np.array_split(my_list, (len(my_list)/2)+1)
print(list_chunked)
