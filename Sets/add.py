"""
   1. The syntax of set add() method is: set.add(elem)

   2. add() method takes a single parameter:

      --> elem - the element that is added to the set should be immutable.

   3. add() method doesn't return any value and returns None.

   4. add() method doesn't add an element to the set if it's already
      present in it.
"""
# Example-1


vowels = {'a', 'e', 'i', 'u'}

vowels.add('o')
print('Vowels are:', vowels)

vowels.add('a')
print('Vowels are:', vowels)
print('\r')

# Example-2


vowels = {'a', 'e', 'u'}
tup = ('i', 'o')

vowels.add(tup)
print('Vowels are:', vowels)

vowels.add(tup)
print('Vowels are:', vowels)
