num = input('Enter the number:- ')

count = len(num)
total = 0
temp = int(num)

while (temp > 0):
    digit = temp % 10
    total += digit**count
    temp //= 10

# lst = [(int(i)**count) for i in list(num)]
# total = sum(lst)

if (int(num) == total):
    print('{} is an armstrong number'.format(int(num)))
else:
    print('{} is not an armstrong number'.format(int(num)))
