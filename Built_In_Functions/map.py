"""
   1. The syntax of map() is: map(function, iterable, ...)

   2. map() Parameter:
      --> function - map() passes each item of the iterable to this function.

      --> iterable - iterable which is to be mapped

      Note- You can pass more than one iterable to the map() function.

   3. map() returns:
      --> The map() function applies a given function to each item of an
          iterable and returns a list of the results.

      --> The returned value from map() (map object) can then be passed to
          functions like list() (to create a list), set() (to create a set)
          and so on.

   4. The map() function applies a given function to each item of an iterable
      (list, tuple etc.) and returns a list of the results.
"""
# Example-1


def calculateSquare(n):
    return n * n


numbers = (1, 2, 3, 4)
result = map(calculateSquare, numbers)
print(result)

numbersSquare = set(result)
print(numbersSquare)
print('\r')

# Example-2(Using lambda function with map)


numbers = (1, 2, 3, 4)
result = map(lambda x: x * x, numbers)
print(result)

numbersSquare = set(result)
print(numbersSquare)
print('\r')

# Example-3(Passing Multiple Iterators to map() Using Lambda)


num1 = [4, 5, 6]
num2 = [5, 6, 7]

result = map(lambda n1, n2: n1 + n2, num1, num2)
print(list(result))
