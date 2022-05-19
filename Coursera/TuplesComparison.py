"""
The comparison operators work with tuples and other sequences. If the first
item is equal, Python goes on to the next element, and so on, until it finds
elements that differ.
"""

# Example-1


a = (0, 1, 2)
b = (5, 1, 2)

print(a < b)
print()

# Example-2


c = (0, 1, 2000000000)
d = (0, 3, 4)

print(c < d)
print()

# Example-3


e = ('Jones', 'Sally')
f = ('Jones', 'Sam')

print(e < f)
print()

# Example-4


e = ('Jones', 'Sally')
f = ('Adams', 'Sam')

print(e > f)
print()
