# Program to print full pyramid using *
"""
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
"""
n = int(input('Enter the number of rows:- '))

# for i in range(1, n+1):
#     char = '* ' * ((2*i)-1)
#     print(char.center(2*(2*n-1)))

for row in range(1, n+1):
    space = 2*(n-row)
    print(" " * space, end="")
    print("* " * (2*row-1))

print('\r')

# Program to print inverted full pyramid using *
"""
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
"""

n = int(input('Enter the number of rows:- '))

# for i in range(n, 0, -1):
#     char = '* ' * ((2*i)-1)
#     print(char.center(2*(2*n-1)))

for row in range(n, 0, -1):
    space = 2*(n-row)
    print(" " * space, end="")
    print("* " * (2*row-1))

print('\r')

# Program to print full pyramid of numbers
"""
        1
      2 3 2
    3 4 5 4 3
  4 5 6 7 6 5 4
5 6 7 8 9 8 7 6 5
"""

n = int(input('Enter the number of rows:- '))

for i in range(1, n+1):
    space = 2*(n-i)
    print(" " * space, end="")
    counter = i-1
    for j in range(i):
        counter += 1
        print(counter, end=" ")
    for k in range(1, i):
        counter -= 1
        print(counter, end=" ")
    print('\r')

print('\r')

# for currentRow in range(1, n+1):
#     x = 2*currentRow-1
#     for i in range(2*n-1):
#         distance = abs(n-1-i)
#         if (distance >= currentRow):
#             print(' ', end=" ")
#         else:
#             print(x - distance, end=" ")
#     print('\r')


# Program to print Pascal's Triangle
"""
     1
    1 1
   1 2 1
  1 3 3 1
 1 4 6 4 1
1 5 10 10 5 1
"""

n = int(input('Enter the number of rows:- '))
coef = 1

for row in range(1, n+1):
    space = (n-row)
    print(" " * space, end="")
    for index in range(0, row):
        if(index == 0):
            coef = 1
        else:
            coef = coef * (row - index)//index
        print(coef, end=" ")
    print('\r')

print('\r')

# Program to print Floyd's Triangle
"""
1
2 3
4 5 6
7 8 9 10
"""

n = int(input('Enter the number of rows:- '))
counter = 0

for i in range(1, n+1):
    for j in range(i):
        counter += 1
        print(counter, end=" ")
    print('\r')

print('\r')
