# Program to print inverted half pyramid using *
"""
* * * * *
* * * *
* * *
* *
*
"""
n = int(input('Enter the number of rows:- '))

# for i in range(1, n+1):
#     print('* ' * (n+1-i))

# for i in range(n, 0, -1):
#     print('* ' * i)

for i in range(n, 0, -1):
    for j in range(1, i+1):
        print('*', end=" ")
    print('\r')

print('\r')

# Program to print inverted half pyramid a using numbers
"""
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
"""

n = int(input('Enter the number of rows:- '))

# for i in range(1, n+1):
#     for j in range(1, (n-i+2)):
#         print(j, end=" ")
#     print('\r')

for i in range(n, 0, -1):
    for j in range(1, i+1):
        print(j, end=" ")
    print('\r')

print('\r')

# Program to print inverted half pyramid using alphabets
"""
E E E E E
D D D D
C C C
B B
A
"""

n = int(input('Enter the number of rows:- '))

# for i in range(1, n+1):
#     for j in range(1, (n-i+2)):
#         print(chr(64 + (n - i + 1)), end=" ")
#         # print(chr(64 + i), end=" ")
#     print('\r')

for i in range(n, 0, -1):
    for j in range(1, i+1):
        print(chr(64 + i), end=" ")
        # print(chr(64 + (n-i+1)), end=" ")
    print('\r')


