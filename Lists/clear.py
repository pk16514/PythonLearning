"""
   1. The syntax of clear() method is: list.clear()

   2. The clear() method doesn't take any parameters.

   3. The clear() method only empties the given list. It doesn't
      return any value.
"""
# Example-1


lst = [{1, 2}, ('a'), ['1.1', '2.2']]
lst.clear()

print('List:', lst)
print('\r')

# Example-2(Emptying the list using del method)


lst = [{1, 2}, ('a'), ['1.1', '2.2']]
del lst
# del list[:]

print('List:', lst)
