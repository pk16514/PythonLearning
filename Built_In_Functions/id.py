"""
   1. The syntax of id() is: id(object)

   2. id() function takes a single parameter 'object'

   3. id() function returns the identity of the object.This is an integer
      that is unique for the given object and remains constant during its
      lifetime.

   4. It's important to note that everything in Python is an object, even
      numbers, and Classes.
"""
# Example-1


class Foo:
    b = 5


dummyFoo = Foo()
print('id of dummyFoo =', id(dummyFoo))

# Example-2


a = 5
print('id of a =', id(a))

b = a
print('id of b =', id(b))

c = 5.0
print('id of c =', id(c))
