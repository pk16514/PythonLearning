"""
Note- The zip() function takes iterables (can be zero or more), aggregates them
      in a tuple, and returns it. Likewise, dict() gives the dictionary.
"""

# Example-1: Using zip and dict methods

index = [1, 2, 3]
languages = ['python', 'c', 'c++']

dictionary = dict(zip(index, languages))
print(dictionary)

# Example-2: Using list comprehension

index = [1, 2, 3]
languages = ['python', 'c', 'c++']

dictionary = {k: v for k, v in zip(index, languages)}
print(dictionary)
