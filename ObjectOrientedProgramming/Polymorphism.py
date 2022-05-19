"""
Note:- 1. Poly means 'many' and morph means 'forms' so that means one thing
          can take multiple forms.

       2. This concept is very important when we talk about software develop
          -ment. So we use this concept a lot when it comes to
          --> Loose Coupling
          --> Dependency Injection
          --> Interface

       3. There are 4 ways to implement polymorphism-
          --> Duck Typing
          --> Operator Overloading
          --> Method Overloading
          --> Method Overriding
"""

# Interface Problem


class Parrot:

    def fly(self):
        print('Parrot can fly')

    def swim(self):
        print("Parrots can't swim")


class Penguin:

    def fly(self):
        print("Penguin can't fly")

    def swim(self):
        print("Penguin can swim")


def flying_test(bird):
    bird.fly()


blu = Parrot()
peggy = Penguin()

flying_test(blu)
flying_test(peggy)
