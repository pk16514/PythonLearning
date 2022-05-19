num = [9, 41, 12, 3, 74, 15]
smallest = None
largest = -1

for value in num:
    if smallest is None:
        smallest = value
    elif (value < smallest):
        smallest = value

for value in num:
    if (value > largest):
        largest = value

print(smallest)
print(largest)
