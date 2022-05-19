"""
Note:- 1. There are 2 types of Attributes(variables)-
          --> Instance Variable(different values for different objects)

          --> class(static) Variable(Same values for all objects)

       2. Namespace is a place where we create and store an object/variable
          Types of Namespace:-
          --> class Namespace- where we create and store all the class
                               variables

          --> Object/Instance Namespace- where we create and store all the
                                         instance variables
"""


class Car:

    wheels = 4

    def __init__(self):
        self.mil = 10
        self.com = 'BMW'


c1 = Car()
c2 = Car()

c1.mil = 8
Car.wheels = 5

print(c1.mil, c1.com, c1.wheels)
print(c2.mil, c2.com, c2.wheels)
