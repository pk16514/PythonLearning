"""
   1. The syntax of issubset() is: A.issubset(B)
      The above code checks if A is a subset of B.

   2. issubset() method returns
      --> True if A is a subset of B

      --> False if A is not a subset of B
"""
# Example-1


A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
C = {1, 2, 4, 5}

print(A.issubset(B))
print(B.issubset(A))
print(A.issubset(C))
print(C.issubset(B))
