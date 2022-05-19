"""
   1. The syntax of the insert() method is: list.insert(index, elem)

   2. The insert() method takes two parameters:
    index - the index where the element needs to be inserted

    element - this is the element to be inserted in the list

   3. The insert() method doesn't return anything; returns None.
      It only updates the current list.
"""
# Example-1


vowel = ['a', 'e', 'i', 'u']
vowel.insert(3, 'o')

print('Updated List:', vowel)
print('\r')

# Example-2


mixed_list = [{1, 2}, [5, 6, 7]]
number_tuple = (3, 4)
mixed_list.insert(1, number_tuple)

print('Updated List:', mixed_list)
print('\r')
