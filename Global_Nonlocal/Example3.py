a = 10
print(id(a))


def something():
    a = 9
    x = globals()['a']
    print(id(x))
    print('inside func.', a)

    globals()['a'] = 16


something()

print('outside func.', a)
