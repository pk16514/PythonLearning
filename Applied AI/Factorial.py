def factorial(num):
    """
    This is a recursive function to find factorial of a no.
    """
    return 1 if num == 1 else (num * factorial(num - 1))


print(factorial.__doc__)
num = int(input('Enter the positive integer:-'))
print("Factorial of {} is {}".format(num, factorial(num)))
