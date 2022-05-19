"""Write a program that repeatedly prompts a user for integer numbers
   until the user enters 'done'. Once 'done' is entered, print out the
   largest and smallest of the numbers. If the user enters anything
   other than a valid number catch it with a try/except and put out an
   appropriate message and ignore the number.
   Enter 7, 2, bob, 10, and 4 and match the output below."""

# Method-1
largest = -1
smallest = None
lst = []
while True:
    num = input("Enter a number: ")
    try:
        if (num == "done"):
            break
        lst.append(int(num))
        for value in lst:
            if (value > largest):
                largest = value

        for value in lst:
            if smallest is None:
                smallest = value
            elif (value < smallest):
                smallest = value
    except ValueError:
        print('Invalid input')

print('Maximum is', largest)
print('Minimum is', smallest)

# Method-2
# lst = []
# while True:
#     num = input("Enter a number: ")
#     try:
#         if (num == "done"):
#             break
#         lst.append(int(num))
#     except ValueError:
#         print('Invalid input')

# if len(lst) > 0:
#     print('Maximum is', max(lst))
#     print('Minimum is', min(lst))
# else:
#     print('Enter the integer value First')
