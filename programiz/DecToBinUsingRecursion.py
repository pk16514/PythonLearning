# Method-1

def Dec_Bin(n):
    lst = []
    if(n > 0):
        x = n % 2
        lst.append(str(x))
        Dec_Bin(n//2)
    lst.sort()
    y = "".join(lst)
    print(y, end="")


n = int(input('Enter a number:- '))

Dec_Bin(n)
print('\r')

# Method-2


def Dec_bin(n):
    if(n > 1):
        Dec_Bin(n//2)
    print(n % 2, end="")


n = int(input('Enter a number:- '))

Dec_Bin(n)
print('\r')
