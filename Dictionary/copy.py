"""
   1. The syntax of copy() is: dict.copy()

   2. It doesn't take any parameters.

   3. This method returns a shallow copy of the dictionary. It doesn't
      modify the original dictionary.

   4. A list can also be copied using the = operator.
      --> When copy() method is used, a new dictionary is created which is
          filled with a copy of the references from the original dictionary.

      --> When = operator is used, a new reference to the original dictionary
          is created.

   5. However, if we need the original dict unchanged when the new list is
      modified, we can use the copy() method.
"""
# Example-1


original = {1: 'one', 2: 'two'}
new = original.copy()

print('Orignal: ', original)
print('New: ', new)
print('\r')

# Example-2(Using = Operator to Copy Dictionaries)


original = {1: 'one', 2: 'two'}
new = original

new.clear()

print('new: ', new)
print('original: ', original)
print('\r')

# Example-3(Using copy() to Copy Dictionaries)


original = {1: 'one', 2: 'two'}
new = original.copy()

new.clear()

print('new: ', new)
print('original: ', original)
