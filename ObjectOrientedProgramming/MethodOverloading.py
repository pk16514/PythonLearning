"""
Note:- 1. In Python, there is no concept of method overloading but then what
          it is. Let's say there is a class which has two methods with the same
          name with different parameters or arguments.
          For Example-
          class Student:
              def average(a, b):
                  pass
              def average(a, b, c):
                  pass
          This is called method overloading.
          But this concept doesn't work in python so we use another trick.
"""


class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self, a=None, b=None, c=None):
        s = 0

        if(a is not None and b is not None and c is not None):
            s = a + b + c
        elif(a is not None and b is not None):
            s = a + b
        else:
            s = a
        return s


s1 = Student(58, 69)
print(s1.sum(5, 9, 6))
print(s1.sum(8, 5))
print(s1.sum())
