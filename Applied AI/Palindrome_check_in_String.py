myStr = input('Enter the String:-')

myStr = myStr.lower()
revStr = reversed(myStr)
# revStr = myStr[::-1]

if list(myStr) == list(revStr):
    print('Given String is Palindrome.')
else:
    print('Given String is not Palindrome.')
