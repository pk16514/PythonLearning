"""
   1. The syntax of the copy() method is:
        new_list = list.copy()

   2. It doesn't take any parameters.

   3. The copy() method returns a new list(shallow copy of original list).
      It doesn't modify the original list.

   4. A list can be copied using the = operator.
      For Example-
      old_list = [1, 2, 3]
​      new_list = old_list

      The problem with copying lists in this way is that if you modify new_list
      old_list is also modified. It is because the new list is referencing or
      pointing to the same old_list object.

   5. However, if we need the original list unchanged when the new list is
      modified, you can use the copy() method.

   6. List slicing also allows shallow copying(very imp).
"""
# Example-1

import copy as cp


my_list = ['cat', 0, 6.7, [1, 2]]
# new_list = my_list.copy()
new_list = cp.deepcopy(my_list)
new_list[3][1] = 4
new_list[1] = 'pk'

print('Copied List:', my_list)
print('\r')

# Example-2(copying a list using slicing)


list = ['cat', 0, [6.7]]

new_list = list[:]
new_list[2].append('dog')

print('Old List:', list)
print('New List:', new_list)
print('\r')

# Example-3(copy using = operator)


old_list = [1, 2, 3]
new_list = old_list

new_list.append('a')

print('New List:', new_list)
print('Old List:', old_list)
