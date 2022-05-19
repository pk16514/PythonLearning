numbers = [10, 15, 18, 30, 40, 50]

# Using While loop
i = 0
product = 1
while(i < len(numbers)):
    product *= numbers[i]
    i += 1

print('Product of all numbers is', product)

# Using for loop
total = 1
for i in numbers:
    total *= i

print('\nProduct is {}'.format(total))
