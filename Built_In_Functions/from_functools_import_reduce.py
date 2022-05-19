"""
   The reduce(fun,seq) function is used to apply a particular function
   passed in its argument to all of the list elements mentioned in the
   sequence passed along.This function is defined in “functools” module.
"""
# Example-1


# from functools import reduce
import functools
import operator

lst1 = [1, 2, 5, 8]


def multiply(x, y):
    return x * y


product = functools.reduce(multiply, lst1)
print(product)
print('\r')

# Example-2


lst2 = [1, 3, 5, 6, 2]

print("The sum of the list elements is : ", end="")
print(functools.reduce(lambda a, b: a + b, lst2))

print("The maximum element of the list is : ", end="")
print(functools.reduce(lambda a, b: a if a > b else b, lst2))
print('\r')

# Example-3(Using Operator Functions)


lst3 = [1, 3, 5, 6, 2]

print("The sum of the list elements is : ", end="")
print(functools.reduce(operator.add, lst3))

print("The product of list elements is : ", end="")
print(functools.reduce(operator.mul, lst3))

print("The concatenated product is : ", end="")
print(functools.reduce(operator.add, ["geeks", "for", "geeks"]))
