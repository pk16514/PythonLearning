"""
   1. The syntax of dir() is: dir([object])

   2. dir() takes maximum of one object.

      --> object (optional) - dir() attempts to return all attributes
                              of this object.

   3. dir() tries to return a list of valid attributes of the object.

      --> If the object has __dir__() method, the method will be called and
          must return the list of attributes.

      --> If the object doesn't have __dir__() method, this method tries to
          find information from the __dict__ attribute (if defined), and from
          type object. In this case, the list returned from dir() may not be
          complete.

      --> If an object is not passed to dir() method, it returns the list of
          names in the current local scope.
"""
# Example-1


number = [1, 2, 3]
print(dir(number))

print('\nReturn Value from empty dir()')
print(dir())
print('\r')

# Example-2(dir() on User-defined Object)


class Person:
    def __dir__(self):
        return ['age', 'name', 'salary']


teacher = Person()
print(dir(teacher))
