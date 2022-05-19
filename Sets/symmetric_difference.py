"""
   1. The syntax of symmetric_difference() is: A.symmetric_difference(B)

   2. The symmetric difference of two sets A and B is the set of elements
      that are in either A or B, but not in their intersection.
"""
# Example-1


A = {'a', 'b', 'c', 'd'}
B = {'c', 'd', 'e'}
C = {}

print(A.symmetric_difference(B))
print(B.symmetric_difference(A))

print(A.symmetric_difference(C))
print(B.symmetric_difference(C))
print('\r')

# Example-2(Using ^ operator)


A = {'a', 'b', 'c', 'd'}
B = {'c', 'd', 'e'}

print(A ^ B)
print(B ^ A)
print(A ^ A)
print(B ^ B)
