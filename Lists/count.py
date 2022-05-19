"""
   1. The syntax of the count() method is: list.count(element)

   2. The count() method takes a single argument:
      --> element- the element to be counted

   3. The count() method returns the number of times element appears in
      the list.
"""
# Example-1


vowels = ['a', 'e', 'i', 'o', 'i', 'u']

count = vowels.count('i')
print('The count of i is:', count)

count = vowels.count('p')
print('The count of p is:', count)
print('\r')

# Example-2


random = ['a', ('a', 'b'), ('a', 'b'), [3, 4]]

count = random.count(('a', 'b'))
print("The count of ('a', 'b') is:", count)

count = random.count([3, 4])
print("The count of [3, 4] is:", count)
