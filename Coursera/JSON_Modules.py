"""
1. JSON stands for JavaScript Object Notation.

2. It looks a lot like the representation of nested dictionaries and lists in
   python when we write them out as literals in a program but with a few small
   differences (e.g., the word null instead of None).

3. When your program receives a JSON-formatted string, generally you will want
   to convert it into a python object, a list or a dictionary.

4. json.loads() takes a string as input and produces a python object
   (a dictionary or a list) as output.

5. The other function we will use is dumps. It does the inverse of loads.
   It takes a python object, typically a dictionary or a list, and returns a
   string, in JSON format. It has a few other parameters. Two useful parameters
   are sort_keys and indent.

6. If sort_keys is true (default: False), then the output of dictionaries will
   be sorted by key.
"""

# Example-1


import json
a_string = """\n\n\n{\n "resultCount":25,\n "results": [\n{"wrapperType":"track",
 "kind":"podcast", "collectionId":10892}]}"""
print(a_string)
d = json.loads(a_string)
print("------")
print(type(d))
print(d.keys())
print(d['resultCount'])
# print(a_string['resultCount'])
print()

# Example-2


def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)


d = {'key1': {'c': True, 'a': 90, '5': 50}, 'key2': {'b': 3, 'c': "yes"}}

print(d)
print('--------')
print(pretty(d))
print(type(pretty(d)))
