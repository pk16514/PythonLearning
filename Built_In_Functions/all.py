"""
   1. The syntax of the all() function is: all(iterable)

   2. The all() function takes a single parameter:
      --> iterable- any iterable (list, tuple, dictionary, etc.)
          which contains the elements

   3. all() function returns:
      --> True- If all elements in an iterable are true

      --> False- If any element in an iterable is false

      Note- In case of empty iterable, it returns True
"""
# Example-1


lst = [1, 3, 4, 5]
print(all(lst))

lst = [0, False]
print(all(lst))

lst = [1, 3, 4, 0]
print(all(lst))

lst = [0, False, 5]
print(all(lst))

lst = []
print(all(lst))
print('\r')

# Example-2


s = "This is good"
print(all(s))

s = '000'
print(all(s))

s = ''
print(all(s))
print('\r')

# Example-3


s = {0: 'False', 1: 'False'}
print(all(s))

s = {1: 'True', 2: 'True'}
print(all(s))

s = {1: 'True', False: 0}
print(all(s))

s = {}
print(all(s))

s = {'0': 'True'}
print(all(s))
