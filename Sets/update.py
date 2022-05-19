"""
   1. The syntax of update() is: set.update(iter1, iter2, iter3,...)

   2. iterable can be any iterable such as list, set, dictionary, string, etc.
      The elements of the iterable are added to the set.

   3. This set update() method returns None (returns nothing).

   4. If dictionaries are passed to the update() method, the keys of the
      dictionaries are added to the set.
"""
# Example-1


A = {'a', 'b'}
B = {1, 2, 3}

result = A.update(B)

print('A =', A)
print('result =', result)
print('\r')

# Example-2


string_alphabet = 'abc'
numbers_set = {1, 2}

numbers_set.update(string_alphabet)
print('numbers_set =', numbers_set)

info_dictionary = {'key': 1, 'lock': 2}
numbers_set = {'a', 'b'}

numbers_set.update(info_dictionary)
print('numbers_set =', numbers_set)
