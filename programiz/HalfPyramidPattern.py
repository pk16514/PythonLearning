# Program to print half pyramid using *
"""
*
* *
* * *
* * * *
* * * * *
"""
n = int(input('Enter the number of rows:- '))

# for i in range(1, n+1):
#     print('* ' * i)

for i in range(1, n+1):
    for j in range(1, i+1):
        print('*', end=" ")
    print('\r')

print('\r')

# Program to print half pyramid a using numbers
"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""

n = int(input('Enter the number of rows:- '))

for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print('\r')

print('\r')

# Program to print half pyramid using alphabets
"""
A
B B
C C C
D D D D
E E E E E
"""

n = int(input('Enter the number of rows:- '))

for i in range(1, n+1):
    for j in range(1, i+1):
        print(chr(64 + i), end=" ")
    print('\r')

print('\r')
