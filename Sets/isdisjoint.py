"""
   1. The syntax of isdisjoint() is: set_a.isdisjoint(set_b)

   2. isdisjoint() method takes a single argument (a set).

      Note-
      You can also pass an iterable (list, tuple, dictionary, and string)
      to isdisjoint(). isdisjoint() method will automatically convert
      iterables to set and checks whether the sets are disjoint or not.

   3. isdisjoint() method returns
      --> True if two sets are disjoint sets
          (if set_a and set_b are disjoint sets in above syntax)

      --> False if two sets are not disjoint sets
"""
# Example-1


A = {1, 2, 3, 4}
B = {5, 6, 7}
C = {4, 5, 6}

print('Are A and B disjoint?', A.isdisjoint(B))
print('Are A and C disjoint?', A.isdisjoint(C))
print('\r')

# Example-2


A = {'a', 'b', 'c', 'd'}
B = ['b', 'e', 'f']
C = '5de4'
D = {1: 'a', 2: 'b'}
E = {'a': 1, 'b': 2}

print('Are A and B disjoint?', A.isdisjoint(B))
print('Are A and C disjoint?', A.isdisjoint(C))
print('Are A and D disjoint?', A.isdisjoint(D))
print('Are A and E disjoint?', A.isdisjoint(E))
