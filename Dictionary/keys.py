"""
   1. The syntax of keys() is: dict.keys()

   2. keys() doesn't take any parameters.

   3. keys() returns a view object that displays a list of all the keys.

      --> When the dictionary is changed, the view object also reflects
          these changes.
"""
# Example-1


person = {'name': 'Phill', 'age': 22, 'salary': 3500.0}
print(person.keys())

empty_dict = {}
print(empty_dict.keys())
print('\r')

# Example-2


person = {'name': 'Phill', 'age': 22, }

print('Before dictionary is updated')
keys = person.keys()
print(keys)

person.update({'salary': 3500.0})
print('\nAfter dictionary is updated')
print(keys)
