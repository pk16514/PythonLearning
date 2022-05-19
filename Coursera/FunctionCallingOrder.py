"""
Please order the code fragments in the order in which the Python interpreter
would evaluate them. x is 2 and y is 3. Now the interpreter is executing
`square(x + sub(square(y), 2 *x))`.

1. look up the variable sub to get the function object
2. look up the variable x, again, to get 2
3. run the square function on input 3, returning the value 9
4. look up the variable square to get the function object
5. run the sub function, passing inputs 9 and 4, returning the value 5
6. multiply 2*2 to get 4
7. look up the variable x to get 2
8. look up the variable y to get 3
9. add 2 and 5 to get 7
10. look up the variable square, again, to get the function object
11. run the square function, again, on input value 7, returning the value 49.
"""
