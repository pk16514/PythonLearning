def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


print('Select any one choice:-')
print('\tSelect 1 for addition')
print('\tSelect 2 for subtraction')
print('\tSelect 3 for multiplication')
print('\tSelect 4 for division')

num1 = int(input('Enter the first number:-'))
num2 = int(input('Enter the second number:-'))
choice = int(input('Enter the choice:-'))

if choice == 1:
    print('Addition of two numbers {} and {} is {}'
          .format(num1, num2, add(num1, num2)))
elif choice == 2:
    print('Difference of two numbers {} and {} is {}'
          .format(num1, num2, sub(num1, num2)))
elif choice == 3:
    print('Multiplication of two numbers {} and {} is {}'
          .format(num1, num2, mul(num1, num2)))
elif choice == 4:
    print('Division of two numbers {} and {} is {}'
          .format(num1, num2, div(num1, num2)))
else:
    print('Invalid Choice')
