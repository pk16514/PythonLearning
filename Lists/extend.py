"""
   1. The syntax of the extend() method is: list1.extend(iterable)

   2. The extend() method takes an iterable such as list, tuple, string etc.

   3. The extend() method modifies the original list. It doesn't return
      any value.

   4. The extend() method adds all the elements of an iterable
      (list, tuple, string etc.) to the end of the list.
"""
# Example-1


languages = ['French', 'English']
languages1 = ['Spanish', 'Portuguese']
languages.extend(languages1)

print('Languages List:', languages)
print('\r')

# Example-2


languages = ['French']
languages_tuple = ('Spanish', 'Portuguese')
languages_set = {'Chinese', 'Japanese'}

languages.extend(languages_tuple)
print('New Language List:', languages)

languages.extend(languages_set)
print('Newer Languages List:', languages)
print('\r')

# Other ways to extend list
# 1. Using '+' operator


a = [1, 2]
b = [3, 4]
a += b

print('a =', a)
print('\r')

# 2. Using the 'list sicing' syntax


a = [1, 2]
b = [3, 4]

a[len(a):] = b

# Output: [1, 2, 3, 4]
print('a =', a)
print('\r')
