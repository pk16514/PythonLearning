"""
   1. The syntax of get() is:
        dict.get(key[, value])

   2. get() method takes maximum of two parameters:
      --> key - key to be searched in the dictionary

      --> value (optional) - Value to be returned if the key is not found.
                             The default value is None.

   3. get() method returns:
      --> the value for the specified key if key is in dictionary.

      --> None if the key is not found and value is not specified.

      --> value if the key is not found and value is specified.

   4. Python get() method Vs dict[key] to Access Elements:-
      --> get() method returns a default value if the key is missing.

      --> However, if the key is not found when you use dict[key],
          KeyError exception is raised.
"""
# Example-1


person = {'name': 'Phill', 'age': 22}

print('Name: ', person.get('name'))
print('Age: ', person.get('age'))
print('Salary: ', person.get('salary'))
print('Salary: ', person.get('salary', 0.0))
print('\r')

# Example-2


person = {}

print('Salary: ', person.get('salary'))
print(person['salary'])
