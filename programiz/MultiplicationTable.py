num = int(input('Enter the positive number for multiplication table:- '))

for i in range(1, 11):
    value = num*i
    print('{} x {} = {}'.format(num, i, value))
