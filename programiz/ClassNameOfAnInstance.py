# Method-1


class Vehicle:
    def name(self, name):
        return name


v = Vehicle()
print(v.__class__.__name__)

# Method-2


class Vehicle:
    def name(self, name):
        return name


v = Vehicle()
print(type(v).__name__)
