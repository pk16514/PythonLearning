num = int(input('Enter the number for fibonacci sequence:- '))

a = 0
b = 1
print('Fibonacci Sequence upto {} terms:- '.format(num))

for i in range(num):
    if (i == 0):
        print(a, end=" ")
    elif (i == 1):
        print(b, end=" ")
    else:
        c = a + b
        print(c, end=" ")
        a = b
        b = c

print('\r')
