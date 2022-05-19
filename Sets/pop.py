"""
   1. The syntax of pop() for sets is: set.pop()

   2. The pop() method doesn't take any arguments.

   3. The pop() method returns an arbitrary (random) element from the set.
      Also, the set is updated and will not contain the element
      (which is returned).

      Note- If the set is empty, TypeError exception is raised.
"""
# Example-1


A = {'a', 'b', 'c', 'd'}

print('Return Value is', A.pop())
print('A = ', A)
