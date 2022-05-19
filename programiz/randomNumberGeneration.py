"""
Note- 1. random.randint(a,b) returns a number N in the inclusive range [a,b],
         meaning a <= N <= b, where the endpoints are included in the range.

      2. random.randrange(a,b) returns a number excluding b.

      3 random.random() returns floating point number b/w 0 & 1
"""

import random

print(random.randint(10, 26))
print(random.randrange(10, 26))
print(random.random())
