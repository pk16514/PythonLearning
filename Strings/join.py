"""
   1. The syntax of the join() method is: string.join(iterable)

   2. The join() method takes an iterable (objects capable of returning its
      members one at a time) as its parameter.

      Some of the example of iterables are:
      --> Native data types - List, Tuple, String, Dictionary and Set.

      --> File objects and objects you define with an __iter()__ or
          __getitem()__method.

   3. The join() method returns a string created by joining the elements of
      an iterable by string separator. If the iterable contains any non-string
      values, it raises a 'TypeError' exception.

   4. The join() method tries to join the keys (not values) of the dictionary
      with the string separator. If the key of the string is not a string,
      it raises a 'TypeError' exception.

   5. A set is an unordered collection of items, so you may get different
      output (order is random).
"""
# Example-1


numList = ['1', '2', '3', '4']
numTuple = ('1', '2', '3', '4')
separator = ', '

print(separator.join(numList))
print(separator.join(numTuple))

s1 = 'abc'
s2 = '123'

print('s1.join(s2):', s1.join(s2))
print('s2.join(s1):', s2.join(s1))

# Example-2


test1 = {'2', '1', '3'}
test2 = {'Python', 'Java', 'Ruby'}
s1 = ', '
s2 = '->->'

print(s1.join(test1))
print(s2.join(test2))

# Example-3


test3 = {'mat': 1, 'that': 2}
test4 = {1: 'mat', 2: 'that'}
s3 = '->'
s4 = ', '

print(s3.join(test3))
print(s4.join(test4))
