"""
   1. The syntax of difference_update() is: A.difference_update(B)

      Here, A and B are two sets. difference_update() updates set A with
      the set difference of A-B.

   2. difference_update() returns None indicating the object (set) is mutated.
"""
# Example-1


A = {'a', 'c', 'g', 'd'}
B = {'c', 'f', 'g'}

result = A.difference_update(B)

print('A = ', A)
print('B = ', B)
print('result = ', result)
