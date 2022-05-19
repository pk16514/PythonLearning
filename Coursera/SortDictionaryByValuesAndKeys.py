"""
In a dictionary there can not be two same keys but same values can exist.
While sorting by values, when the first item is same, it sorts by second
item.
"""

# By Keys


d = {'a': 10, 'c': 1, 'b': 22}

print(sorted(d.items()))

# By Values


d = {'a': 10, 'c': 10, 'b': 22}
temp = []
x = d.items()

for key, value in sorted(x):
    temp.append((value, key))

print(sorted(temp))
print(sorted(temp, reverse=True))
