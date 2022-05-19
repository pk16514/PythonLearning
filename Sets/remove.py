"""
   1. The syntax of the remove() method is: set.remove(element)

   2. The remove() method takes a single element as an argument and
      removes it from the set.

   3. The remove() removes the specified element from the set and updates
      the set. It doesn't return any value.
      Note- If the element passed to remove() doesn't exist, KeyError exception
            is thrown.
"""
# Example-1


language = {'English', 'French', 'German'}
language.remove('German')

print('Updated language set:', language)
print('\r')

# Example-2


animal = {'cat', 'dog', 'rabbit', 'guinea pig'}
animal.remove('fish')

print('Updated animal set:', animal)
