num1 = int(input('Enter the 1st number:- '))
num2 = int(input('Enter the 2nd number:- '))

for i in range(num1, num2):
    count = len(str(i))
    lst = [(int(j)**count) for j in list(str(i))]
    total = sum(lst)

    if (i == total):
        print(i)
    else:
        pass
