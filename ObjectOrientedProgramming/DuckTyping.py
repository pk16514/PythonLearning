"""
Note:- 1. In duck typing, the type or the class of an object is less important
          than the method it defines. Using Duck Typing, we do not check types
          at all. Instead, we check for the presence of a given method or
          attribute.

       2. Duck-typing emphasis what the object can really do, rather than what
          the object is.

       3. If there is an object which is IDE and it has a method execute that
          said we are not concerned about which class object it is what we are
          concerned about it should have that method which is execute and that
          is called duck-typing.
"""


class Pycharm:

    def execute(self):
        print('compiling')
        print('running')


class MyEditor:

    def execute(self):
        print('Spell Check')
        print('Convention Check')
        print('compiling')
        print('running')


class Laptop:

    def code(self, ide):
        ide.execute()


ide = MyEditor()

lap1 = Laptop()
lap1.code(ide)

