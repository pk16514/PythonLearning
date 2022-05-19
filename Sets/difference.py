"""
   1. The syntax of difference() method in Python is: A.difference(B)
      Here, A and B are two sets. The following syntax is equivalent to A-B.

   2. difference() method returns the difference between two sets which is
      also a set. It doesn't modify original sets.
"""
# Example-1


A = {'a', 'b', 'c', 'd'}
B = {'c', 'f', 'g'}

print(A.difference(B))
print(B.difference(A))
print('\r')

# Example-2(Using - operator)


A = {'a', 'b', 'c', 'd'}
B = {'c', 'f', 'g'}

print(A-B)
print(B-A)
