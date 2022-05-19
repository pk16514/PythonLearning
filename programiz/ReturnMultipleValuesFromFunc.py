# Example-1


def name():
    return "John", "Armin"


# print the tuple with the returned values
print(name())

# get the individual items
name_1, name_2 = name()
print(name_1, name_2)
print('\r')

# Example-2


def name():
    n1 = "John"
    n2 = "Armin"

    return {1: n1, 2: n2}


names = name()
print(names)
print('\r')
