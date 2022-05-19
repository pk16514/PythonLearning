"""
Note:- 1. There are 3 types of Behaviours(Methods)-
          --> Instance Method(use with instance variables)
              * Types of Instance Methods-
                --> Accessor Methods-
                    used for fetching the instance variables

                --> Mutator Methods-
                    used for modifying the instance variable

          --> class Method(used with class variables)

          --> static Method
              This method does not concern with instance or class variable
              we use this method for something extra.

       2. In case of instance variable we use 'self' but in case of class
          variable we use 'cls' in the argument along with decorators
          '@classmethod'.

       3. for static method, we do not need any argument but we use a decorator
          @staticmethod.
"""


class Student:

    school = 'Telusko'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3

    def get_m1(self):
        return self.m1

    def set_m1(self, value):
        self.m1 = value

    @classmethod
    def getSchool(cls):
        return cls.school

    @staticmethod
    def info():
        print('This is student class.......in abc module')


s1 = Student(34, 47, 32)
s2 = Student(89, 32, 12)

print(s1.avg())
print(s2.avg())
print(s1.get_m1())
print(Student.getSchool())
Student.info()
