"""
   1. The syntax of the list index() method is: list.index(element, start, end)

   2. The list index() method can take a maximum of three arguments:
      --> element - the element to be searched

      --> start (optional) - start searching from this index

      --> end (optional) - search the element up to this index

   3. The index() method returns the index of the given element in the list.
      If the element is not found, a ValueError exception is raised.

      Note- The index() method only returns the first occurrence of the
            matching element.
"""
# Example-1


vowels = ['a', 'e', 'i', 'o', 'i', 'u']

index = vowels.index('e')
print('The index of e:', index)

index = vowels.index('i')
print('The index of i:', index)
print('\r')

# Example-2


alphabets = ['a', 'e', 'i', 'o', 'g', 'l', 'i', 'u']

index = alphabets.index('e')
print('The index of e:', index)

index = alphabets.index('i', 4)
print('The index of i:', index)

index = alphabets.index('i', 3, 5)
print('The index of i:', index)
print('\r')

# Example-3


vowels = ['a', 'e', 'i', 'o', 'u']

index = vowels.index('p')
print('The index of p:', index)
print('\r')
