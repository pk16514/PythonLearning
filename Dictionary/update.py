"""
   1. The syntax of update() is: dict.update([other])

   2. The update() method takes either a dictionary or an iterable object
      of key/value pairs (generally tuples).

      Note- If update() is called without passing parameters, the dictionary
            remains unchanged.

   3. update() method updates the dictionary with elements from a dictionary
      object or an iterable object of key/value pairs.

      It doesn't return any value (returns None).
"""
# Example-1


d = {1: "one", 2: "three", 3: 'three'}

d1 = {2: "two"}
d.update(d1)
print(d)


d1 = {3: "three"}
d.update(d1)
print(d)
print('\r')

# Example-2(update() When Tuple is Passed)


d = {'x': 2}

d.update(y=3, z=0)
print(d)
