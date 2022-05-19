"""
   1. The syntax of split() is: string.split([separator [, maxsplit]])

   2. split() method takes a maximum of 2 parameters:
      --> separator (optional)-
         It is a delimiter. The string splits at the specified separator.
         If the separator is not specified, any whitespace (space, newline
         etc.) string is a separator.

      --> maxsplit (optional)-
          The maxsplit defines the maximum number of splits.The default value
          of maxsplit is -1, meaning, no limit on the number of splits.

   3. split() breaks the string at the separator and returns a list of strings.

   4. If maxsplit is specified, the list will have the maximum of maxsplit+1
      items.
"""
# Example-1


text = 'Love thy neighbor'

print(text.split())

grocery = 'Milk, Chicken, Bread'

print(grocery.split(', '))
print(grocery.split(':'))
print('\r')

# Example-2

grocery = 'Milk, Chicken, Bread, Butter'

print(grocery.split(', ', 2))
print(grocery.split(', ', 1))
print(grocery.split(', ', 5))
print(grocery.split(', ', 0))
