"""
   1. The syntax of union() is: set.union(*other_sets)
      Note-
      * is not part of the syntax. It is used to indicate that the method
      can take 0 or more arguments.

   2. The union() method returns a new set with elements from the set and
      all other sets (passed as an argument).

      Note- If the argument is not passed to union(), it returns a shallow
            copy of the set.
"""
# Example-1


A = {'a', 'c', 'd'}
B = {'c', 'd', 2}
C = {1, 2, 3}

print('A U B =', A.union(B))
print('B U C =', B.union(C))
print('A U B U C =', A.union(B, C))
print('A.union() =', A.union())
print('\r')

# Example-2(Union using | operator)


A = {'a', 'c', 'd'}
B = {'c', 'd', 2}
C = {1, 2, 3}

print('A U B =', A | B)
print('B U C =', B | C)
print('A U B U C =', A | B | C)
# print('A U B U C =', A | (B, C))
