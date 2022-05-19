"""
   1. The syntax of setdefault() is:
        dict.setdefault(key[, default_value]))

   2. setdefault() takes a maximum of two parameters:
      --> key- the key to be searched in the dictionary

      --> default_value(optional)-
          key with a value default_value is inserted to the dictionary if the
          key is not in the dictionary. If not provided, the default_value
          will be None.

   3. setdefault() returns:
      --> value of the key if it is in the dictionary

      --> None if the key is not in the dictionary and default_value is not
          specified

      --> default_value if key is not in the dictionary and default_value is
          specified
"""
# Example-1


person = {'name': 'Phill', 'age': 22}

age = person.setdefault('age')
print('person = ', person)
print('Age = ', age)
print('\r')

# Example-2


person = {'name': 'Phill'}
salary = person.setdefault('salary')
print('person = ', person)
print('salary = ', salary)

age = person.setdefault('age', 22)
print('person = ', person)
print('age = ', age)
