"""
Note:- 1. The object of Inner Class can be created inside the __init__
           of outer class but outside of inner class. Or we can create
           outside the outer class.
           syntax would be 'obj = OuterClass.innerclass()'
"""


class Student:

    school = 'Telusko'

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        # self.lap = self.Laptop()
        # comment above line if create obj of inner class outside

    def show(self):
        print(self.name, self.rollno)
        # self.lap.show()
        # comment above line if create obj of inner class outside

    class Laptop:

        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 8

        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = Student('Naveen', 2)
s2 = Student('Jenny', 3)

lap1 = Student.Laptop()
lap2 = Student.Laptop()

s1.show()
lap1.show()
s2.show()
lap2.show()

# print(s1.lap.brand)

# lap1 = s1.lap
# lap2 = s2.lap

print(id(lap1))
print(id(lap2))
