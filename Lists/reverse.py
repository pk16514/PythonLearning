"""
   1. The syntax of the reverse() method is: list.reverse()

   2. The reverse() method doesn't take any arguments.

   3. The reverse() method doesn't return any value. It updates the
      existing list.
"""
# Example-1


systems = ['Windows', 'macOS', 'Linux']
print('Original List:', systems)

systems.reverse()
print('Updated List:', systems)
print('\r')

# Example-2(Using Slice Operator)


systems = ['Windows', 'macOS', 'Linux']
print('Original List:', systems)

reversed_list = systems[::-1]
print('Updated List:', reversed_list)
print('\r')

# Example-3(Accessing Element in reverse order)


systems = ['Windows', 'macOS', 'Linux']
systems_updated = reversed(systems)
print(systems)
print(systems_updated)

for o in systems_updated:
    print(o)
