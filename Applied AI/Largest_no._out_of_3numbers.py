a, b, c = input('Enter the numbers:- ').split(', ')
a = int(a)
b = int(b)
c = int(c)

if(a > b and a > c):
    print('{} is the largest number'.format(a))
elif(b > a and b > c):
    print('{} is the largest number'.format(b))
else:
    print('{} is the largest number'.format(c))
