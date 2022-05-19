# Referencing & Aliasing


a = [81, 82, 83]
b = [81, 82, 83]
print(a is b)

b = a
print(a == b)
print(a is b)

b[0] = 5
print(a)
print()

# Cloning using slice operator


a = [81, 82, 83]

b = a[:]       # make a clone using slice
print(a == b)
print(a is b)

b[0] = 5

print(a)
print(b)
print()

# Important Example-
"""
Beware of using something like item = item + new_item with mutable objects
though because it creates a new object because concatanation creates new obj.
However, when we use += then that doesn't happen.
"""

b = ['q', 'u', 'i']
z = ['a', 'e']
b = z
print(b)
print(z)

b = b + z    # b += z
print(b)
print(z)
