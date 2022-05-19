num = int(input('Enter the number whose factorial you want to know:- '))
fact = 1

if (num < 0):
    print('Sorry, Factorial does not exist for negative numbers.')
elif (num == 0):
    print('The factorial of 0 is 1.')
else:
    for i in range(1, num+1):
        fact *= i
    print('The factorial of {} is {}'.format(num, fact))
