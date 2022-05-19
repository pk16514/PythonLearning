# Method-1


num1 = 0
num2 = 1
n = int(input('Enter the integer:- '))

for i in range(1, n + 1):
    if i == 1:
        print(num1, end=" ")
    elif i == 2:
        print(num2, end=" ")
    else:
        num3 = num1 + num2
        num1 = num2
        num2 = num3
        print(num3, end=" ")
print('\n')

# Method-2(Using Recursive function)


def fibonacci(num):
    """
    Recursive function to print fibonacci sequence
    """
    return num if num <= 1 else fibonacci(num - 1) + fibonacci(num - 2)


nterms = int(input('Enter the number of terms:- '))
print('fibonacci sequence')
for num in range(nterms):
    print(fibonacci(num))
