# Program-1


"""
Write a function called beginning that takes a list as input and contains
a while loop that only stops once the element of the list is the string
‘bye’. What is returned is a list that contains up to the first 10 strings,
regardless of where the loop stops. (i.e., if it stops on the 32nd element,
the first 10 are returned. If “bye” is the 5th element, the first 4 are
returned.) If you want to make this even more of a challenge, do this
without slicing
"""


def beginning(lst):
    i = 0
    updated_list = []
    while(i < 10 and i < len(lst) and lst[i] != 'bye'):
        updated_list.append(lst[i])
        i += 1
    return updated_list


print(beginning([]))
print()

# Program-2


"""
Write a function called stop_at_four that iterates through a list of numbers.
Using a while loop, append each number to a new list until the number 4
appears. The function should return the new list.
"""


def stop_at_four(lst):
    i = 0
    lst1 = []
    while i < len(lst) and lst[i] != 4:
        lst1.append(lst[i])
        i += 1
    return lst1


print(stop_at_four([]))
print()
