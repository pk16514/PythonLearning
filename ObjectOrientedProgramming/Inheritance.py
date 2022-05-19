# Single Level Inheritance


class A:
    def feature1(self):
        print('feature 1 is working')

    def feature2(self):
        print('feature 2 is working')


class B(A):
    def feature3(self):
        print('feature 3 is working')

    def feature4(self):
        print('feature 4 is working')


a = A()

a.feature1()
a.feature2()
print('\r')

b = B()

b.feature1()
b.feature2()
b.feature3()
b.feature4()
print('\r')

# Multi Level Inheritance


class X:
    def feature1(self):
        print('feature 1 is working')

    def feature2(self):
        print('feature 2 is working')


class Y(X):
    def feature3(self):
        print('feature 3 is working')

    def feature4(self):
        print('feature 4 is working')


class Z(Y):
    def feature5(self):
        print('feature 5 is working')


x = X()

x.feature1()
x.feature2()
print('\r')

y = Y()

y.feature1()
y.feature2()
y.feature3()
y.feature4()
print('\r')

z = Z()
z.feature1()
z.feature2()
z.feature3()
z.feature4()
z.feature5()
print('\r')

# Multiple Inheritance


class K:
    def feature1(self):
        print('feature 1 is working')

    def feature2(self):
        print('feature 2 is working')


class Q:
    def feature3(self):
        print('feature 3 is working')

    def feature4(self):
        print('feature 4 is working')


class J(K, Q):
    def feature5(self):
        print('feature 5 is working')


k = K()

k.feature1()
k.feature2()
print('\r')

q = Q()

q.feature3()
q.feature4()
print('\r')

j = J()
j.feature1()
j.feature2()
j.feature3()
j.feature4()
j.feature5()
print('\r')
