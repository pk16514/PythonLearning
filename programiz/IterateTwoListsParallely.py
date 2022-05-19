"""
The loop runs until the shorter list stops unless other conditions are passed.
"""

list_1 = [1, 2, 3, 4]
list_2 = ['a', 'b', 'c']

for i, j in zip(list_1, list_2):
    print(i, j)
