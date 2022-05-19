"""
   1. The syntax of discard() in Python is: s.discard(element)

   2. discard() method takes a single element x and removes it from the
      set (if present).

   3. discard() removes element x from the set if the element is present.
      This method returns None (meaning, absence of a return value).
"""
# Example-1


numbers = {2, 3, 4, 5}

numbers.discard(3)
print('numbers = ', numbers)

numbers.discard(10)
print('numbers = ', numbers)
print('\r')

# Example-2


numbers = {2, 3, 5, 4}

print(numbers.discard(3))
print('numbers =', numbers)
