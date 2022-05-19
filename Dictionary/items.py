"""
   1. The syntax of items() method is: dictionary.items()

   2. items() method doesn't take any parameters.

   3. items() method returns a view object that displays a list of
      a given dictionary's (key, value) tuple pair.
"""
# Example-1


sales = {'apple': 2, 'orange': 3, 'grapes': 4}

print(sales.items())
print('\r')

# Example-2


sales = {'apple': 2, 'orange': 3, 'grapes': 4}

items = sales.items()
print('Original items:', items)

del[sales['apple']]
print('Updated items:', items)
