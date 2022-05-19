"""
   1. The syntax of intersection() in Python is: set.intersection(*other_sets)
      Note-
      * is not part of the syntax. It is used to indicate that the method
      can take 0 or more arguments.

   2. intersection() method returns the intersection of set with all the sets
      (passed as argument).

      Note- If the argument is not passed to intersection(), it returns a
            shallow copy of the set.
"""
# Example-1


A = {2, 3, 5, 4}
B = {2, 5, 100}
C = {2, 3, 8, 9, 10}

print(B.intersection(A))
print(B.intersection(C))
print(A.intersection(C))
print(C.intersection(A, B))
print('\r')

# Example-2(Using & Operator)


A = {100, 7, 8}
B = {200, 4, 5}
C = {300, 2, 3, 7}
D = {100, 200, 300}

print(A & C)
print(A & D)
print(A & C & D)
print(A & B & C & D)
