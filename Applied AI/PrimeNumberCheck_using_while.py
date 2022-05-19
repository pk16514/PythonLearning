num = int(input('Enter a Number:-'))

isDivisible = False
i = 2

while (i < num):
    if (num % i == 0):
        isDivisible = True
        print('{} is divisible by {}'.format(num, i))
        break
    i += 1

if isDivisible:
    print('{} is not a prime number'.format(num))
else:
    print('{} is a prime number'.format(num))
