"""
Note:- 1. Everytime we execute the program, we create two different objects
          and they allocate new space in heap memory.

       2. Size of the object depends upon the no. of variables and size of
          the variables.

       3. Constructor is responsible to assign the memory or to calculate the
          memory required.

       4. self is used because when we call update method, it doesn't know
          which one to update c1 or c2. So, the object which calls for that
          method passes itself into self.
"""


class Computer:

    def __init__(self):
        self.name = 'Naveen'
        self.age = 28

    def update(self):
        self.age = 30

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False


c1 = Computer()
c2 = Computer()

print(id(c1))
print(id(c2))

c1.name = 'Rashi'
c1.age = 12

c1.update()

if c1.compare(c2):
    print('They are same')
else:
    print('They are different')

print(c1.name)
print(c2.name)
