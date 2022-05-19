"""
   1. The syntax of the remove() method is: list.remove(element)

   2. The remove() method takes a single element as an argument and removes
      it from the list.

      Note- If the element doesn't exist, it throws ValueError:
      list.remove(x): x not in list exception.

   3. The insert() method doesn't return anything(returns None).

   4. If a list contains duplicate elements, the remove() method
      only removes the first matching element.
"""
# Example-1


animals = ['cat', 'dog', 'rabbit', 'guinea pig']
animals.remove('rabbit')

print('Updated animals list: ', animals)
print('\r')

# Example-2


animals = ['cat', 'dog', 'dog', 'guinea pig', 'dog']
animals.remove('dog')

print('Updated animals list: ', animals)
print('\r')

# Example-3


animals = ['cat', 'dog', 'rabbit', 'guinea pig']
animals.remove('fish')

print('Updated animals list: ', animals)
print('\r')
