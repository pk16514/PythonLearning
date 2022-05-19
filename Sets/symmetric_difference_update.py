"""
   1. The syntax of symmetric_difference_update() is:
        A.symmetric_difference_update(B)

   2. The symmetric_difference_update() returns None (returns nothing).
      Rather, it updates the set calling it.
"""
# Example-1


A = {'a', 'c', 'd'}
B = {'c', 'd', 'e'}

result = A.symmetric_difference_update(B)

print('A =', A)
print('B =', B)
print('result =', result)
