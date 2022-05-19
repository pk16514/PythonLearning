start = int(input('Enter the start value of the interval:-'))
end = int(input('Enter the start value of the interval:-'))

for i in range(start, end):
    isDivisible = False
    if (i > 1):
        for j in range(2, i):
            if (i % j == 0):
                isDivisible = True
                print('{} is divisible by {}'.format(i, j))
                # break
        if isDivisible:
            print('{} is not a prime number'.format(i))
        else:
            print('{} is a prime number'.format(i))
    else:
        print('1 is not a prime number')

# num1 = int(input('Enter 1st Number:- '))
# num2 = int(input('Enter 2nd Number:- '))

# for i in range(num1, num2):
#     isDivisible = False
#     if (i >= 2):
#         for j in range(2, i):
#             if (i % j == 0):
#                 isDivisible = True
#                 break
#         if isDivisible:
#             pass
#         else:
#             print(i)
#     else:
#         pass
