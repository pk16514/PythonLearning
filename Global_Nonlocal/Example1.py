"""
Note:- 1. Global variable can not be edited.

       2. Statements outside functions can not access inside func. variables.

       3. Statements inside functions can access global variables.
          (priority will be given to local variables inside functions)

       4. To edit global variable inside func., we need to use 'global' keyword
          if local variable is absent.

       5. We can not write same local as well as global variable inside
          func. together

       6. We can access all the global variable together with same local
          variable inside a func. using globals()['global variable']
"""

x = 10  # global variable


def function(n):
    # x = 5  # local variable
    y = 8  # local variable
    global x
    x += 45
    print(x, y)
    print(n, 'I have printed')


function('This is me')
print(x)
