"""
   1. The syntax of intersection_update() is:
        set.intersection_update(*other_sets)
      Note-
      * is not part of the syntax. It is used to indicate that the method
      can take 0 or more arguments.

   2. This method returns None (meaning it does not have a return value).
      It only updates the set calling the intersection_update() method.
"""
# Example-1


A = {1, 2, 3, 4}
B = {2, 3, 4, 5}

result = A.intersection_update(B)

print('result =', result)
print('A =', A)
print('B =', B)
print('\r')

# Example-2


A = {1, 2, 3, 4}
B = {2, 3, 4, 5, 6}
C = {4, 5, 6, 9, 10}

result = C.intersection_update(B, A)

print('result =', result)
print('C =', C)
print('B =', B)
print('A =', A)
