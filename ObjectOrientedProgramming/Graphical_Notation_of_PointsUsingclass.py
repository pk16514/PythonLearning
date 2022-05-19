"""
To be able to reason about class variables and instance variables, it is helpful to know the
rules that the python interpreter uses. That way, you can mentally simulate what the interpreter does.

--> When the interpreter sees an expression of the form <obj>.<varname>, it:
     1. Checks if the object has an instance variable set. If so, it uses that value.
     2. If it doesn’t find an instance variable, it checks whether the class has a class
        variable. If so it uses that value.
     3. If it doesn’t find an instance or a class variable, it creates a runtime error
        (actually, it does one other check first, which you will learn about in the next chapter).

--> When the interpreter sees an assignment statement of the form <obj>.<varname> = <expr>, it:
     1. Evaluates the expression on the right-hand side to yield some python object;
     2. Sets the instance variable <varname> of <obj> to be bound to that python object.
        Note that an assignment statement of this form never sets the class variable; it
        only sets the instance variable.

    In order to set the class variable, you use an assignment statement of the form <varname> = <expr>
    at the top-level in a class definition, like on line 36 in the code above to set the class variable
    printed_rep.

--> In case you are curious, method definitions also create class variables. Thus, in the code above,
    graph becomes a class variable that is bound to a function/method object. p1.graph() is evaluated by:
     1. looking up p1 and finding that it’s an instance of Point
     2. looking for an instance variable called graph in p1, but not finding one
     3. looking for a class variable called graph in p1’s class, the Point class; it finds a
        function/method object
     4. Because of the () after the word graph, it invokes the function/method object, with
        the parameter self bound to the object p1 points to.
"""


class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    printed_rep = '*'

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def graph(self):
        row = []
        size = max(self.x, self.y) + 2
        for j in range(size - 1):
            if (j + 1) == int(self.y):
                special_row = str((j + 1) % 10) + (" " * (int(self.x) - 1)) + self.printed_rep
                row.append(special_row)
            else:
                row.append(str((j + 1) % 10))
        row.reverse()
        x_axis = ""
        for i in range(size):
            x_axis += str(i % 10)
        row.append(x_axis)

        return "\n".join(row)


p1 = Point(2, 3)
p2 = Point(3, 12)
print(p1.graph())
print()
print(p2.graph())
