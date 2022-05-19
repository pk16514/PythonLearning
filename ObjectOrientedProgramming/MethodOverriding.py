# Example-


class A:
    def show(self):
        print('in A show')


class B(A):
    pass


b = B()
b.show()
print('\r')

# Example-2


class A:
    def show(self):
        print('in A show')


class B(A):
    def show(self):
        print('in B show')


b = B()
b.show()
print('\r')

# Example-3


class A:
    ls = 'pk1'

    def __init__(self):
        self.ls = 3


class B(A):
    pass
    ls = 'pk2'

    def __init__(self):
        self.lt = 9


b = B()
print(b.ls)
