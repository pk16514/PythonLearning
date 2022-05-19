"""
   1. The syntax of popitem() is: dict.popitem()

   2. The popitem() doesn't take any parameters.

   3. The popitem() method removes and returns the (key, value) pair from
      the dictionary in the Last In, First Out (LIFO) order.

      --> Returns the latest inserted element (key,value) pair from
          the dictionary.

      --> Removes the returned element pair from the dictionary.

      Note- 1. Before Python 3.7, the popitem() method returned and removed
               an arbitrary element (key, value) pair from the dictionary.

            2. The popitem() method raises a KeyError error if the dictionary
               is empty.
"""
# Example-1


person = {'name': 'Phill', 'age': 22, 'salary': 3500.0}
result = person.popitem()

print('Return Value = ', result)
print('person = ', person)
print('\r')

person['profession'] = 'Plumber'
result = person.popitem()

print('Return Value = ', result)
print('person = ', person)
