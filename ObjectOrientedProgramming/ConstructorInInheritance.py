"""
Note:- 1. When we create an object of sub-class it will first try to find
          init of sub-class if it is not found then it will init of super
          class.

       2. Three principle of MRO:-
          --> The first principle is always visit for the subclass before going
              for its base classes. If class B is inherited from A, it will
              visit B first and then goes to A.

          --> The second principle is, if any class is inherited from several
              classes, it searches in the order from left to right in the base
              classes. For example, if class C is inherited from A and B,
              syntactically class C(A, B), then first it will search in A and
              then in B.

          --> The third principle is that it will not visit any class more than
              once.That means a class in the inheritance hierarchy is traversed
              only once exactly.
"""
# Example-1


class A:
    def __init__(self):
        print('in A init')

    def feature1(self):
        print('feature 1-A is working')

    def feature2(self):
        print('feature 2 is working')


class B:
    def __init__(self):
        print('in B init')

    def feature3(self):
        print('feature 1-B is working')

    def feature4(self):
        print('feature 4 is working')


class C(A, B):
    def __init__(self):
        super().__init__()
        print('in C init')

    def feat(self):
        super().feature2()


c = C()
c.feat()
print('\r')

# Example-2


class Animal:
    def __init__(self, Animal):
        print(Animal, 'is an animal.')


class Mammal(Animal):
    def __init__(self, mammalName):
        print(mammalName, 'is a warm-blooded animal.')
        super().__init__(mammalName)


class NonWingedMammal(Mammal):
    def __init__(self, NonWingedMammal):
        print(NonWingedMammal, "can't fly.")
        super().__init__(NonWingedMammal)


class NonMarineMammal(Mammal):
    def __init__(self, NonMarineMammal):
        print(NonMarineMammal, "can't swim.")
        super().__init__(NonMarineMammal)


class Dog(NonMarineMammal, NonWingedMammal):
    def __init__(self):
        print('Dog has 4 legs.')
        super().__init__('Dog')


d = Dog()
print('')
bat = NonMarineMammal('Bat')
