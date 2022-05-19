"""
   1. The syntax of enumerate() is: enumerate(iterable, start=0)

   2. enumerate() method takes two parameters:
      --> iterable - a sequence, an iterator, or objects that supports
                     iteration

      --> start(optional)- enumerate() starts counting from this number.
                           If start is omitted, 0 is taken as start.

   3. enumerate() method adds counter to an iterable and returns it. The
      returned object is a enumerate object.

      You can convert enumerate objects to list and tuple using list() and
      tuple() method respectively.
"""
# Example-1


grocery = ['bread', 'milk', 'butter']
enumerateGrocery = enumerate(grocery)

print(type(enumerateGrocery))
print(list(enumerateGrocery))

enumerateGrocery = enumerate(grocery, 10)
print(list(enumerateGrocery))

# Example-2


grocery = ['bread', 'milk', 'butter']

for item in enumerate(grocery):
    print(item)

print('\n')
for count, item in enumerate(grocery):
    print(count, item)

print('\n')
for count, item in enumerate(grocery, 100):
    print(count, item)
