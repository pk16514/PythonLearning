"""
print out the user’s screen name and when their account was created.
"""


import json
from res import res

print(type(res))
string = json.dumps(res, indent=4)
# print(string)
print(type(string))
print(res.keys())
res1 = res['statuses']
print(type(res1))
for identity in res1:
    print(identity['user']['screen_name'], end=" ")
    print(identity['created_at'])
