
nested = {'data': ['finding', 23, ['exercises', 'hangout', 34]],
          'window':
          ['part', 'whole', [], 'sum', ['math', 'calculus', 'algebra',
           'geometry', 'statistics', ['physics', 'chemistry', 'biology']]]}

"""
Check to see if the string data is a key in nested, if it is, assign True
to the variable data, otherwise assign False.

Check to see if the integer 24 is in the value of the key data, if it is
then assign to the variable twentyfour the value of True, otherwise False.

Check to see that the string 'whole' is not in the value of the key window.
If it's not, then assign to the variable whole the value of True, otherwise
False.

Check to see if the string 'physics' is a key in the dictionary nested.
If it is, assign to the variable physics, the value of True, otherwise False.
"""

if nested['data']:
    data = True
else:
    data = False

if 24 in nested['data']:
    twentyfour = True
else:
    twentyfour = False

x = list(nested.values())

if 'whole' not in x[1]:
    whole = True
else:
    whole = False

if 'physics' in nested.keys():
    physics = True
else:
    physics = False
