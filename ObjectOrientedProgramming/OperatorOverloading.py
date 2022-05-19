"""
Note:- 1. Whenever we try to print an object behind the scene, it calls __str__
          method internally.

       2. Operator internal Magic Methods-
          --> + = __add__(self, other)
          --> - = __sub__(self, other)
          --> * = __mul__(self, other)
          --> / = __truediv__(self, other)
          --> // = __floordiv__(self, other)
          --> ** = __pow__(self, other)
          --> % = __mod__(self, other)
          --> < = __lt__(self, other)
          --> <= = __le__(self, other)
          --> > = __gt__(self, other)
          --> >= = __ge__(self, other)
          --> != = __ne__(self, other)
"""


class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1, m2)
        return s3

    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False

    def __str__(self):
        return f'{self.m1} {self.m2}'


s1 = Student(58, 69)
s2 = Student(69, 65)

s3 = s1 + s2
print(s3.m1)
print(s3.m2)

if(s1 > s2):
    print('s1 wins')
else:
    print('s2 wins')

a = 9
print(a)
print(a.__str__())

print(s1)
print(s1.__str__())
print(str(s1))
print(format(s1))

# Here it is showing the value of a but it is showing the address of s1
# not the value. But I want to see the value so for that we need to override
# __str__ method.
