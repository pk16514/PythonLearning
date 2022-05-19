# # Method-1


# def ComputeLCM(num1, num2):
#     smaller = num2 if num1 > num2 else num1

#     for i in range(1, smaller + 1):
#         if (num1 % i == 0) and (num2 % i == 0):
#             HCF = i
#     LCM = (num1*num2)//HCF
#     return LCM


# z = ComputeLCM(8, 20)
# print(z)

# Method-2


def ComputeLCM(num1, num2):
    greater = num1 if num1 > num2 else num2

    while True:
        if(greater % num1 == 0 and greater % num2 == 0):
            LCM = greater
            break
        greater += 1
    return LCM


z = ComputeLCM(8, 25)
print(z)
