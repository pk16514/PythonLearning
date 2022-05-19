"""
   1. The syntax of isinstance() is: isinstance(object, classinfo)

   2. isinstance() takes two parameters:
      --> object- object to be checked

      --> classinfo- class, type, or tuple of classes and types

   3. isinstance() returns:
      --> True if the object is an instance or subclass of a class or any
          element of the tuple

      --> False otherwise

      Note- If classinfo is not a type or tuple of types, a TypeError
            exception is raised.

   4. The isinstance() function checks if the object (first argument) is an
      instance or subclass of classinfo class (second argument).
"""
# Example-1


class Foo:
    a = 5


fooInstance = Foo()

print(isinstance(fooInstance, Foo))
print(isinstance(fooInstance, (list, tuple)))
print(isinstance(fooInstance, (list, tuple, Foo)))
print('\r')

# Example-2


numbers = [1, 2, 3]

result = isinstance(numbers, list)
print(numbers, 'instance of list?', result)

result = isinstance(numbers, dict)
print(numbers, 'instance of dict?', result)

result = isinstance(numbers, (dict, list))
print(numbers, 'instance of dict or list?', result)

number = 5

result = isinstance(number, list)
print(number, 'instance of list?', result)

result = isinstance(number, int)
print(number, 'instance of int?', result)
