"""
Note:- 1. Nonlocal variables are used in nested functions whose local
          scope is not defined.

       2. This means that the variable can be neither in the local nor
          the global scope.

       3. If we change the value of a nonlocal variable, the changes
          appear in the local variable.
"""


def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)


outer()
