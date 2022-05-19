year = int(input('Enter the year:- '))

if (year % 4 == 0):
    if (year % 100 == 0 and year % 400 == 0):
        print('{} is Leap year'.format(year))
    elif (year % 100 != 0):
        print('{} is Leap year'.format(year))
    else:
        print('{} is not a Leap year'.format(year))
else:
    print('{} is not a Leap year'.format(year))
