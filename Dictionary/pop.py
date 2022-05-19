"""
   1. The syntax of pop() method is: dictionary.pop(key[, default])

   2. pop() method takes two parameters:
      --> key- which is to be searched for removal

      --> default_value-
          value which is to be returned when the key is not in the dictionary

   3. The pop() method returns:
      --> If key is found- removed/popped element from the dictionary

      --> If key is not found- value specified as the second argument(default)

      --> If key is not found and default argument is not specified-
          KeyError exception is raised
"""
# Example-1


sales = {'apple': 2, 'orange': 3, 'grapes': 4}
element = sales.pop('apple')

print('The popped element is:', element)
print('The dictionary is:', sales)
print('\r')

# Example-2


sales = {'apple': 2, 'orange': 3, 'grapes': 4}

element = sales.pop('guava', 'banana')
print('The popped element is:', element)
print('The dictionary is:', sales)
print('\r')

# Example-3


sales = {'apple': 2, 'orange': 3, 'grapes': 4}

element = sales.pop('guava')
