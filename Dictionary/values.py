"""
   1. The syntax of values() is: dictionary.values()

   2. values() method doesn't take any parameters.

   3. values() method returns a view object that displays a list of all
      values in a given dictionary.
"""
# Example-1


sales = {'apple': 2, 'orange': 3, 'grapes': 4}

print(sales.values())
print('\r')

# Example-2


sales = {'apple': 2, 'orange': 3, 'grapes': 4}

values = sales.values()
print('Original items:', values)

del[sales['apple']]
print('Updated items:', values)
