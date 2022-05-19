# Method-1
# a = int(input())
# b = int(input())
# sets1 = set()
# sets2 = set()

# for i in range(1, a+1):
#     if (a % i == 0):
#         sets1.add(i)

# for j in range(1, b+1):
#     if (b % j == 0):
#         sets2.add(j)

# HCF = max(sets1 & sets2)
# print(HCF)

# Method-2
# Using Functions

def ComputeHCF(num1, num2):
    """
    Computing HCF of two numbers.
    """
    smaller = num2 if num1 > num2 else num1

    for i in range(1, smaller + 1):
        if (num1 % i == 0) and (num2 % i == 0):
            hcf = i
    return hcf


num1 = 78
num2 = 117
# Method to extract doc string
print(ComputeHCF.__doc__)
print('H.C.F Of two numbers {} and {} is {}'
      .format(num1, num2, ComputeHCF(num1, num2)))
