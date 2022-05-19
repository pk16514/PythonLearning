"""
   1. The syntax of the pop() method is: list.pop(index)

   2. The pop() method takes a single argument (index).

      --> index(optional)-
          The argument passed to the method is optional. If not passed, the
          default index -1 is passed as an argument(index of the last item).

      Note- If the index passed to the method is not in range, it throws
            IndexError: pop index out of range exception.

   3. The pop() method returns the item present at the given index. This item
      is also removed from the list.
"""
# Example-1


languages = ['Python', 'Java', 'C++', 'French', 'C']
return_value = languages.pop(3)

print('Return Value:', return_value)
print('Updated List:', languages)
print('\r')

# Example-2


languages = ['Python', 'Java', 'C++', 'Ruby', 'C']

print('When index is not passed:')
print('Return Value:', languages.pop())
print('Updated List:', languages)

print('\nWhen -1 is passed:')
print('Return Value:', languages.pop(-1))
print('Updated List:', languages)

print('\nWhen -3 is passed:')
print('Return Value:', languages.pop(-3))
print('Updated List:', languages)
print('\r')
