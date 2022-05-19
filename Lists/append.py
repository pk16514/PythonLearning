"""
   1. The syntax of the append() method is: list.append(item)

   2. The method takes a single argument-
      --> item - an item to be added at the end of the list

      The item can be numbers, strings, dictionaries, another list, and so on.

   3. The method doesn't return any value (returns None).
"""
# Example-1


animals = ['cat', 'dog', 'rabbit']
animals.append('guinea pig')

print('Updated animals list: ', animals)
print('\r')

# Example-2


animals = ['cat', 'dog', 'rabbit']
wild_animals = ['tiger', 'fox']
animals.append(wild_animals)

print('Updated animals list: ', animals)
print('\r')
