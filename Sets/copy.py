"""
   1. The syntax of the copy() method is: set.copy()

   2. It doesn't take any parameters.

   3. The copy() method returns a shallow copy of the set.

   4. A set can also be copied using = operator in Python.
      For Example-
      numbers = {1, 2, 3, 4}
      new_numbers = numbers

      The problem with copying the set in this way is that if you modify
      the numbers set, the new_numbers set is also modified.

   5. However, if we need the original set to be unchanged when the new
      set is modified, you can use the copy() method.
"""
# Example-1


numbers = {1, 2, 3, 4}
new_numbers = numbers.copy()
new_numbers.add(5)

print('numbers: ', numbers)
print('new_numbers: ', new_numbers)
print('\r')

# Example-2


numbers = {1, 2, 3, 4}
new_numbers = numbers
new_numbers.add(5)

print('numbers: ', numbers)
print('new_numbers: ', new_numbers)
